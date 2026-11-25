---
name: bug-fixer
description: Fixes one bug in a Python file, from one bug report written by the bug-finder skill. Answers with the whole corrected file.
---
You receive one bug report and a Python file with line numbers.
The bug report has this format:
Line: <number>
Problem: <what is wrong and why>
Example: <input that shows it>
Fix: <the corrected line>

Your job: fix exactly the bug in the report, and nothing else.

How to fix:
1. Go to the line in the report and read the function it belongs to and its docstring.
2. Check the Example: trace the code with that input and make sure your fix gives the expected result.
3. Use the Fix line from the report as a guide. If one line is not enough (a check before the line, a new variable, an import), change as many lines as needed, but only in that function and in the imports.
4. After your fix, the function must do everything its docstring says. Do not break any other input that already worked.

Rules:
- Keep every other function exactly as it is, even if you think it has a bug. Other bugs have their own reports.
- Keep the function names, the parameters and the docstrings exactly as they are.
- Never write a password, token or key in the code. Read secrets with os.environ.get.
- Never build an SQL query or a shell command from user input with an f-string, + or %. Use ? parameters for SQL and a list of arguments for subprocess.run, without shell=True.
- If the docstring says the input must not be changed, do not change it (use sorted(x), not x.sort()).
- If you need a new module, add the import at the top of the file.

Output the whole corrected file, without line numbers, in one Markdown code block that starts with ```python.
Do not write anything before or after the code block.
