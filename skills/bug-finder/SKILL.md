You receive a Python file with line numbers.
Review EVERY function independently and compare its implementation with its docstring.

For each function:
1. Identify the exact behavior required by the docstring.
2. Trace the code using a concrete input.
3. Check boundary values carefully.
4. Check unusual inputs and security risks.
5. Report every verified contradiction between the code and the docstring, and every security risk.

Boundary checks:
- For "N or more" or "at least N", check N-1, N, and N+1.
- For a minimum length, check an input with exactly that length while satisfying all other requirements.
- For a bounded range, check values below, inside, and above the range, including both endpoints.

Unusual inputs:
- Check an empty list, an empty string, a string with only spaces, zero, and negative numbers.
- If the docstring says what happens for one of these inputs, the code must return exactly that and must not raise an exception.
- A crash (ZeroDivisionError, IndexError, KeyError, ...) on an input the docstring allows is a bug.

Security checks:
- A password, token, or key written directly in the code is a bug. Fix: read it from an environment variable, for example os.environ.get("NAME", "").
- User input placed inside an SQL string (f-string, + or %) is SQL injection. Fix: use a ? placeholder and pass the value as a parameter.
- User input placed inside a shell command (os.system, shell=True) is command injection. Fix: validate the input and pass a list of arguments to subprocess.run without shell=True.
- User input used in a file path without checking it stays inside the allowed folder is path traversal.
- For a security bug, the Example is an attack input and what it does, for example find_user(db, "x' OR '1'='1") returns a row, expected None.

Do not stop after finding the first bug.
Do not invent bugs in functions that already behave correctly.

For every bug, output exactly this format:
Line: <integer line number>
Problem: <function name, what is wrong, and why>
Example: <concrete function call, actual result, and expected result>
Fix: <corrected Python line only>

Separate reports with a blank line.
Each report must begin with the literal text Line: followed by its line number.
Do not use bullet points, bold formatting, headings, or Markdown code fences in the output.
