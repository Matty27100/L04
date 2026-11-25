# Bug reports for exercise4.py

Line: 4
Problem: ADMIN_PASSWORD is written directly in the source code. Anyone who can read the repository (or its git history) knows the admin password, and it cannot be changed without changing the code.
Example: "admin123" appears in exercise4.py, so check_admin("admin123") returns True for anyone who read the code, expected the secret not to be in the code
Fix: ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "")

Line: 14
Problem: find_user puts the username straight into the SQL string with an f-string. This is SQL injection: an attacker can change the query and get a row for a username that does not exist.
Example: find_user(db, "x' OR '1'='1") returns the row of ana, expected None
Fix: return db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
