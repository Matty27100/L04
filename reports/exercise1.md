# Bug reports for exercise1.py

Line: 2
Problem: The docstring "true for even numbers" is ambiguous and does not clearly describe the function's behavior or return value. It lacks specificity about what input values are accepted or what the output should be. For example, it does not state that the function returns a boolean or that it checks if a number is divisible by 2. This can lead to confusion for users reading the documentation.
Example: Calling is_even(3) — the function correctly returns False, but the docstring does not clearly communicate that it returns a boolean indicating whether the number is even.
Fix: Change the docstring to "Returns True if the number is even (divisible by 2), False otherwise."

Line: 7
Problem: The docstring "area of a rectangle." is incomplete and lacks essential details such as the units, input types, or expected return value. It does not specify that the function takes two arguments (width and height) or that it returns a numerical value representing the area.
Example: Calling rectangle_area(5, 3) returns 15, but the docstring does not clarify that the inputs are positive numbers or that the output is in square units.
Fix: Change the docstring to "Returns the area of a rectangle given its width and height (in square units)."

Line: 12
Problem: The docstring "twice the number n" is vague and does not specify the return type or whether the input is expected to be a number. It lacks clarity about the function's behavior or the expected output format.
Example: Calling double(4.5) returns 9.0, but the docstring does not indicate that it works with floating-point numbers or that it returns a number twice the input.
Fix: Change the docstring to "Returns twice the input value n (as a number)."
