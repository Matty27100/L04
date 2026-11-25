You receive one bug report and the Python file.
Write one test that proves the reported bug.

Use the example input from the bug report.
Assert the correct result required by the function's docstring.
The test must fail on the buggy code and pass after the bug is fixed.
If the buggy code raises an exception on the example input, still call the function normally and assert the expected result: the exception makes the test fail, which is correct.

Security bugs:
- Hard-coded secret: assert the secret text is not in the source, for example assert "admin123" not in open(exercise4.__file__).read().
- SQL injection: create the database inside the test with sqlite3.connect(":memory:"), create the table and insert one real row. Assert the attack input returns None and the real value still returns its row.
- Command injection: request the no_shell fixture as a test argument. It records every os.system and subprocess.run call instead of running it. Call the function with the attack input and assert the expected result and that no call contains the attack text.

Output only Python code: one function whose name starts with test_.
The exercise functions are already imported in the test file, and the modules os, sqlite3, subprocess and pytest are imported too.
Do not include imports, explanations, Markdown code fences, or implementations of the exercise functions.
