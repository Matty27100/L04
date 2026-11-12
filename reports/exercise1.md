# Bug reports for exercise1.py

Line: 3
Problem: The condition `n % 2 == 1` checks if a number is odd, not even. For even numbers, the remainder when divided by 2 should be 0, not 1. Thus, the function incorrectly returns `True` for odd numbers and `False` for even numbers.
Example: Input `4` (even) → Actual result: `False` (incorrect) → Expected result: `True`
Fix: Line 3 should be `return n % 2 == 0`

Line: 8
Problem: The function `rectangle_area` incorrectly returns the sum of width and height instead of the product. The area of a rectangle is calculated as width × height, not width + height.
Example: Input `width=3`, `height=4` → Actual result: `7` → Expected result: `12`
Fix: Line 8 should be `return width * height`

Line: 13
Problem: The function `double(n)` adds 2 to `n`, but the docstring says "twice the number n", which means it should return `n * 2`, not `n + 2`.
Example: Input `5` → Actual result: `7` → Expected result: `10`
Fix: Line 13 should be `return n * 2`
