# Bug reports for exercise4.py

Line: 4
Problem: Hardcoded admin password in source code is a security vulnerability. The password "admin123" is directly written in the code, making it easily discoverable and exploitable. This violates security best practices and exposes the system to brute-force or dictionary attacks.
Example: An attacker can simply read the source code to obtain the password.
Fix: Replace line 4 with: ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "admin123")

Line: 14
Problem: SQL injection vulnerability. The function directly interpolates the username into a SQL query using f-string, allowing an attacker to inject malicious SQL code. For example, passing ' OR '1'='1' could return all users or crash the query.
Example: find_user(db, "x' OR '1'='1") returns a row, expected None (or at least not all users).
Fix: Replace line 14 with: return db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
