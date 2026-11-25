# L04 homework: results

Pipeline per file: bug-finder (skill 1) -> test-writer (skill 2) -> run tests -> fix -> run the same tests again. For the homework the fix is done by the bug-fixer (skill 3).

A test is **good** when it fails on the original code and passes on the fixed code.

## Summary

| File | Functions | Bug reports | Tests | Fail before fix | Pass after fix | Good tests | Fixed by |
|---|---|---|---|---|---|---|---|
| exercise1.py | 3 | 3 | 3 | 3/3 | 3/3 | 3/3 | by hand (branch fix/exercise1) |
| exercise2.py | 3 | 3 | 3 | 3/3 | 3/3 | 3/3 | by hand (branch fix/exercise2) |
| exercise3.py | 3 | 3 | 3 | 3/3 | 3/3 | 3/3 | by hand (branch fix/exercise3) |
| exercise4.py | 2 | 2 | 2 | 2/2 | 2/2 | 2/2 | by hand (branch fix/exercise4) |
| homework.py | 5 | 6 | 6 | 6/6 | 6/6 | 6/6 | bug-fixer skill |

## exercise1.py

| # | Function | Level | Line | Bug (from the report) | Test | Before fix | After fix | Good |
|---|---|---|---|---|---|---|---|---|
| 1 | `is_even` |  | 3 | The condition `n % 2 == 1` checks if a number is odd, not even. For even numbers, the r... | `test_r1_is_even` | FAILED | PASSED | yes |
| 2 | `rectangle_area` |  | 8 | The function `rectangle_area` incorrectly returns the sum of width and height instead o... | `test_r2_rectangle_area` | FAILED | PASSED | yes |
| 3 | `double` |  | 13 | The function `double(n)` adds 2 to `n`, but the docstring says "twice the number n", wh... | `test_r3_double` | FAILED | PASSED | yes |

## exercise2.py

| # | Function | Level | Line | Bug (from the report) | Test | Before fix | After fix | Good |
|---|---|---|---|---|---|---|---|---|
| 1 | `is_passing` |  | 3 | is_passing function incorrectly checks for "greater than 5" instead of "5 or more" as s... | `test_r1_is_passing` | FAILED | PASSED | yes |
| 2 | `clamp` |  | 13 | clamp function has a logical error in its implementation. It uses max(low, min(x, low))... | `test_r2_clamp` | FAILED | PASSED | yes |
| 3 | `is_valid_password` |  | 8 | is_valid_password requires more than 8 characters (len(password) > 8), but the docstrin... | `test_r3_is_valid_password` | FAILED | PASSED | yes |

## exercise3.py

| # | Function | Level | Line | Bug (from the report) | Test | Before fix | After fix | Good |
|---|---|---|---|---|---|---|---|---|
| 1 | `average` |  | 3 | average divides by len(numbers) without checking for an empty list. The docstring says... | `test_r1_average_empty_list` | FAILED | PASSED | yes |
| 2 | `first_word` |  | 8 | first_word takes text.split()[0] without checking that there is a word. The docstring s... | `test_r2_first_word_empty_text` | FAILED | PASSED | yes |
| 3 | `percent` |  | 13 | percent divides by total without checking for zero. The docstring says the result is 0... | `test_r3_percent_zero_total` | FAILED | PASSED | yes |

## exercise4.py

| # | Function | Level | Line | Bug (from the report) | Test | Before fix | After fix | Good |
|---|---|---|---|---|---|---|---|---|
| 1 | `ADMIN_PASSWORD` |  | 4 | ADMIN_PASSWORD is written directly in the source code. Anyone who can read the reposito... | `test_r1_no_hardcoded_admin_password` | FAILED | PASSED | yes |
| 2 | `find_user` |  | 14 | find_user puts the username straight into the SQL string with an f-string. This is SQL... | `test_r2_find_user_sql_injection` | FAILED | PASSED | yes |

## homework.py

| # | Function | Level | Line | Bug (from the report) | Test | Before fix | After fix | Good |
|---|---|---|---|---|---|---|---|---|
| 1 | `celsius_to_fahrenheit` | 1 (easy) | 7 | celsius_to_fahrenheit subtracts 32, but the docstring gives the formula F = C * 9 / 5 +... | `test_r1_celsius_to_fahrenheit_boiling_point` | FAILED | PASSED | yes |
| 2 | `is_leap_year` | 2 (easy-medium) | 14 | is_leap_year forgets the 400 rule from the docstring: a year divisible by 100 is a leap... | `test_r2_is_leap_year_2000` | FAILED | PASSED | yes |
| 3 | `median` | 3 (medium) | 21 | median takes the middle element without sorting the numbers first. The docstring says t... | `test_r3_median_unsorted_list` | FAILED | PASSED | yes |
| 4 | `median` | 3 (medium) | 24 | median does not handle the empty list. The docstring says an empty list has median None... | `test_r4_median_empty_list` | FAILED | PASSED | yes |
| 5 | `binary_search` | 4 (medium-hard) | 31 | binary_search stops when low == high, so the last remaining candidate is never compared... | `test_r5_binary_search_last_element` | FAILED | PASSED | yes |
| 6 | `ping` | 5 (hard) | 47 | ping puts host straight into a shell command with os.system and an f-string. This is co... | `test_r6_ping_command_injection` | FAILED | PASSED | yes |
