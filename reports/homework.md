# Bug reports for homework.py

Line: 7
Problem: celsius_to_fahrenheit subtracts 32, but the docstring gives the formula F = C * 9 / 5 + 32. Every result is 64 degrees too low.
Example: celsius_to_fahrenheit(100) returns 148.0, expected 212.0
Fix: return c * 9 / 5 + 32

Line: 14
Problem: is_leap_year forgets the 400 rule from the docstring: a year divisible by 100 is a leap year if it is also divisible by 400. The code returns False for every year divisible by 100.
Example: is_leap_year(2000) returns False, expected True
Fix: return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

Line: 21
Problem: median takes the middle element without sorting the numbers first. The docstring says the middle value once they are sorted, so any unsorted list gives a wrong answer.
Example: median([3, 1, 2]) returns 1, expected 2
Fix: ordered = sorted(numbers)

Line: 24
Problem: median does not handle the empty list. The docstring says an empty list has median None, but for [] the count is even, so the code reads numbers[-1] and raises IndexError.
Example: median([]) raises IndexError, expected None
Fix: return (numbers[middle - 1] + numbers[middle]) / 2 if numbers else None

Line: 31
Problem: binary_search stops when low == high, so the last remaining candidate is never compared. A target at the end of the search (or in a one-element list) is reported as missing.
Example: binary_search([1, 3, 5], 5) returns -1, expected 2
Fix: while low <= high:

Line: 47
Problem: ping puts host straight into a shell command with os.system and an f-string. This is command injection: host is never checked, so an attacker can run any command after a ;. The docstring says invalid hosts must return False without running anything.
Example: ping("example.com; rm -rf ~") runs "ping -c 1 example.com; rm -rf ~" in the shell and returns True, expected False and no command run
Fix: return bool(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9.-]*", host)) and subprocess.run(["ping", "-c", "1", host], capture_output=True).returncode == 0
