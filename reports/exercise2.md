# Bug reports for exercise2.py

Line: 3
Problem: is_passing function incorrectly checks for "greater than 5" instead of "5 or more" as specified in the docstring. The condition should include 5 itself, but the current implementation uses > 5, which excludes 5. For example, a grade of 5 should return True, but the function returns False.
Example: is_passing(5) -> False, expected True
Fix: return grade >= 5

Line: 13
Problem: clamp function has a logical error in its implementation. It uses max(low, min(x, low)), which simplifies to low regardless of x. The correct behavior should be to clamp x between low and high, so it should use min(max(x, low), high). The current code incorrectly returns low for all inputs.
Example: clamp(10, 5, 15) -> 5, expected 10
Fix: return max(low, min(x, high))

Line: 8
Problem: is_valid_password requires more than 8 characters (len(password) > 8), but the docstring says "at least 8 characters". A password with exactly 8 characters and a digit is rejected.
Example: is_valid_password("abcdefg1") -> False, expected True
Fix: return len(password) >= 8 and any(c.isdigit() for c in password)
