# Bug reports for exercise3.py

Line: 3
Problem: average function crashes on empty list due to division by zero in the condition, though docstring says it returns 0 for empty list
Example: average([]) returns ZeroDivisionError, expected 0
Fix: return sum(numbers) / len(numbers) if numbers else 0

Line: 8
Problem: first_word function splits the text and returns the first word, but if the text contains only whitespace, it returns empty string, which is correct per docstring. However, the code uses text.split() which is correct, but the condition text.split() is not necessary — it's redundant since split() on whitespace returns empty list when text is all whitespace, and that's handled correctly. The logic is correct, but the code could be simplified. However, no behavior mismatch is found; the docstring says "first word or empty string if text is empty", and the function correctly returns "" for empty or whitespace-only strings.
Fix: no change needed

Line: 13
Problem: percent function returns part / total * 100 when total is not zero, which is correct. However, if part is negative or non-integer, the function still works as expected. The docstring only specifies behavior when total is zero. There is no issue with negative numbers or edge cases like part being zero. The function correctly returns 0 when total is 0. No behavior mismatch found.
Fix: no change needed
