# Bug reports for exercise3.py

Line: 3
Problem: average divides by len(numbers) without checking for an empty list. The docstring says an empty list has average 0, but the code raises ZeroDivisionError.
Example: average([]) raises ZeroDivisionError, expected 0
Fix: return sum(numbers) / len(numbers) if numbers else 0

Line: 8
Problem: first_word takes text.split()[0] without checking that there is a word. The docstring says the result is "" if the text is empty, but the code raises IndexError.
Example: first_word("") raises IndexError, expected ""
Fix: return text.split()[0] if text.split() else ""

Line: 13
Problem: percent divides by total without checking for zero. The docstring says the result is 0 if total is 0, but the code raises ZeroDivisionError.
Example: percent(1, 0) raises ZeroDivisionError, expected 0
Fix: return part / total * 100 if total != 0 else 0
