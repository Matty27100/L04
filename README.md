# L04

    exercise1.py ... exercise4.py   the code with bugs (one file per exercise)
    skills/bug-finder/              skill 1: writes the bug reports
    skills/test-writer/             skill 2: writes a test for each bug
    reports/                        the bug reports, saved by the notebook
    tests/                          the tests, saved by the notebook
    lab_helpers.py                  helpers for the notebook

## Lab rounds

Each exercise is on its own branch, made from `main`: `fix/exercise1` ... `fix/exercise4`
(bug reports, tests and the fix by hand).

## Homework (branch `homework`)

    skills/bug-fixer/               skill 3: fixes each bug from its bug report (answers with the whole fixed file)
    homework.py                     5 functions, from easy to hard, each with bugs
    homework_helpers.py             fix_bugs() for skill 3, and homework_report() for the results table
    reports/homework.md             bug reports for homework.py (skill 1)
    tests/test_homework.py          one test per bug report (skill 2)
    reports/homework_report.md      the results table

| Level | Function | Kind of bug |
|---|---|---|
| 1 (easy) | `celsius_to_fahrenheit` | wrong operation |
| 2 (easy-medium) | `is_leap_year` | missing rule (the 400 years exception) |
| 3 (medium) | `median` | unsorted input and empty list (2 bugs) |
| 4 (medium-hard) | `binary_search` | off-by-one in the loop condition |
| 5 (hard) | `ping` | command injection through `os.system` |

In the notebook, after `setup(...)` and `load_model()`:

```python
from homework_helpers import *
find_bugs("homework.py")          # skill 1 -> reports/homework.md
write_tests("homework.py")        # skill 2 -> tests/test_homework.py
run_tests("homework.py")          # all tests FAIL on the buggy code
fix_bugs("homework.py")           # skill 3 fixes each bug, one report at a time
run_tests("homework.py")          # the same tests now PASS
homework_report(["homework.py"])  # -> reports/homework_report.md
```

`fix_bugs` refuses an answer that is not valid Python, removes a function, or changes nothing,
and keeps the file as it was for that report. To start over: `git checkout <commit> -- homework.py`
with the commit that added `homework.py`.
