You receive a Python file with line numbers.
Review EVERY function independently and compare its implementation with its docstring.

For each function:
1. Identify the exact behavior required by the docstring.
2. Trace the code using a concrete input.
3. Check boundary values carefully.
4. Report every verified contradiction between the code and the docstring.

Boundary checks:
- For "N or more" or "at least N", check N-1, N, and N+1.
- For a minimum length, check an input with exactly that length while satisfying all other requirements.
- For a bounded range, check values below, inside, and above the range, including both endpoints.

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
