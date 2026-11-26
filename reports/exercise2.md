# Bug reports for exercise2.py

Line: 7
Problem: The docstring states "At least 8 characters and at least one digit", but the function does not validate that the password contains at least one digit correctly. The `any(c.isdigit() for c in password)` part is correct, but the function does not explicitly check for the length and digit condition in a way that matches the docstring's clarity. However, the actual implementation is correct. There is no bug here.  
Example: Input: "pass123" → Output: True → Expected: True  
Fix: None

Line: 11
Problem: The docstring says "x, limited to the range from low to high", which is correct, but the function uses `min(max(x, low), high)`, which is logically correct. However, if `x` is not a number (e.g., a string), it will raise a TypeError. The function lacks type checking or input validation, which may lead to unexpected behavior.  
Example: Input: x="abc", low=0, high=10 → Output: TypeError → Expected: Should handle non-numeric input gracefully  
Fix: Add type checking to ensure x is numeric. For example:  
```python
def clamp(x, low, high):
    """x, limited to the range from low to high"""
    if not isinstance(x, (int, float)):
        raise TypeError("x must be a number")
    return min(max(x, low), high)
```
