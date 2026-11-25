"""Homework helpers for L04: skill 3 (bug-fixer) and the results report.

In the notebook, after the lab setup (setup + load_model):

    from homework_helpers import *
    find_bugs("homework.py")       # skill 1: bug reports   -> reports/homework.md
    write_tests("homework.py")     # skill 2: one test each -> tests/test_homework.py
    run_tests("homework.py")       # the tests fail on the buggy code
    fix_bugs("homework.py")        # skill 3: fixes each bug from its report
    run_tests("homework.py")       # the same tests now pass
    homework_report(["homework.py"])   # -> reports/homework_report.md
"""
import ast
import difflib
import os
import re
import shutil
import subprocess
import sys
import tempfile

import lab_helpers
from lab_helpers import check, find_bugs, run_tests, skill, split_reports, write_tests  # noqa: F401


def _git(*args):
    r = subprocess.run(["git", *args], capture_output=True, text=True)
    return r.stdout.strip()


def _numbered(code):
    return "\n".join(f"{i:3d} | {l}" for i, l in enumerate(code.splitlines(), 1))


def _code_block(text):
    """The code of the first ```python block in the answer, or the whole answer if there is none."""
    m = re.search(r"`{3}(?:python)?\n(.*?)`{3}", text, re.S)
    code = (m.group(1) if m else text).strip("\n")
    return "\n".join(re.sub(r"^\s*\d+\s\|\s?", "", l) if re.match(r"^\s*\d+\s\|", l) else l
                     for l in code.splitlines()) + "\n"    # drop line numbers if the model kept them


def _functions(code):
    return {n.name for n in ast.walk(ast.parse(code)) if isinstance(n, ast.FunctionDef)}


def _problem(old, new):
    """Why the new file cannot replace the old one, or None if it can."""
    try:
        ast.parse(new)
    except SyntaxError as e:
        return f"the answer is not valid Python ({e.msg}, line {e.lineno})"
    missing = _functions(old) - _functions(new)
    if missing:
        return "the answer removed the function(s) " + ", ".join(sorted(missing))
    if new.strip() == old.strip():
        return "the answer did not change anything"
    return None


# ---------------------------------------------------------------- skill 3: fixes

def fix_bugs(file):
    """Runs your bug-fixer skill on each bug report, one report at a time, and saves the fixed file.
    Each fix starts from the file as the previous fix left it, so the fixes add up."""
    name = file.replace(".py", "")
    path = f"reports/{name}.md"
    if not os.path.exists(path):
        return check("bug reports found", False, f'run find_bugs("{file}") first')
    reports = split_reports(open(path).read())
    applied = 0
    for k, r in enumerate(reports, 1):
        old = open(file).read()
        answer = lab_helpers.ask(skill("bug-fixer"), f"## Bug report\n{r}\n\n## The file {file}\n{_numbered(old)}",
                                 max_new_tokens=1500)
        new = _code_block(answer)
        problem = _problem(old, new)
        print(f"---------------- fix for bug report {k}")
        if problem:
            check(f"fix {k} not applied", False, problem)
            continue
        with open(file, "w") as f:
            f.write(new)
        applied += 1
        print("".join(difflib.unified_diff(old.splitlines(True), new.splitlines(True), file, file, n=1)))
    return check(f"{applied}/{len(reports)} fixes applied to {file}", applied == len(reports) and applied > 0,
                 "a fix the skill could not write: improve skills/bug-fixer/SKILL.md and run fix_bugs again")


# ---------------------------------------------------------------- the results

def original_commit(file):
    """The commit that added the file, so the code before any fix."""
    commits = _git("log", "--diff-filter=A", "--format=%H", "--", file).split()
    return commits[-1] if commits else None


def _statuses(name, cwd=None):
    r = subprocess.run([sys.executable, "-m", "pytest", f"tests/test_{name}.py", "-q", "-rA", "--no-header",
                        "-p", "no:cacheprovider"], capture_output=True, text=True, cwd=cwd)
    return {l.split(" ", 1)[1].split(" - ")[0].split("::")[-1]: l.split(" ", 1)[0]
            for l in (r.stdout + r.stderr).splitlines() if l.startswith(("PASSED", "FAILED", "ERROR"))}


def _owner(code, line):
    """(function name, level comment) of the function that contains the line."""
    lines = code.splitlines()
    for n in ast.walk(ast.parse(code)):
        if isinstance(n, ast.FunctionDef) and n.lineno <= line <= n.end_lineno:
            above = lines[n.lineno - 2] if n.lineno >= 2 else ""
            m = re.match(r"\s*#\s*Level\s*(.+)", above)
            return n.name, (m.group(1).strip() if m else "")
    for n in ast.parse(code).body:                         # a module-level line, e.g. a constant
        if isinstance(n, ast.Assign) and n.lineno <= line <= n.end_lineno:
            return ", ".join(t.id for t in n.targets if isinstance(t, ast.Name)) or "?", ""
    return "?", ""


def round_results(file):
    """For each test: which bug report it comes from, and whether it fails before the fix and passes after."""
    name = file.replace(".py", "")
    commit = original_commit(file)
    original = _git("show", f"{commit}:{file}") + "\n"
    reports = split_reports(open(f"reports/{name}.md").read())
    with tempfile.TemporaryDirectory() as tmp:
        shutil.copytree("tests", os.path.join(tmp, "tests"))
        with open(os.path.join(tmp, file), "w") as f:
            f.write(original)
        before = _statuses(name, cwd=tmp)
    after = _statuses(name)
    rows = []
    for test, status in after.items():
        m = re.match(r"test_r(\d+)_", test)
        k = int(m.group(1)) if m else 0
        line = int(re.search(r"Line:\s*(\d+)", reports[k - 1]).group(1)) if 0 < k <= len(reports) else 0
        problem = re.search(r"Problem:\s*(.+)", reports[k - 1]).group(1) if 0 < k <= len(reports) else ""
        function, level = _owner(original, line) if line else ("?", "")
        rows.append(dict(file=file, report=k, line=line, function=function, level=level, test=test,
                         problem=problem, before=before.get(test, "MISSING"), after=status,
                         good=status == "PASSED" and before.get(test) in ("FAILED", "ERROR")))
    return dict(file=file, reports=len(reports), tests=len(rows), good=sum(r["good"] for r in rows),
                functions=len(_functions(original)), rows=rows)


def _short(text, n=90):
    text = text.replace("|", "\\|")
    return text if len(text) <= n else text[: n - 3].rstrip() + "..."


def homework_report(files, path="reports/homework_report.md", results=None, fixed_by="bug-fixer skill"):
    """Writes a Markdown table with the results of each file: bug reports, tests, before and after the fix.
    `results` can add rounds computed elsewhere (round_results on another branch), with their own "fixed_by"."""
    results = list(results or []) + [dict(round_results(f), fixed_by=fixed_by) for f in files]
    out = ["# L04 homework: results", "",
           "Pipeline per file: bug-finder (skill 1) -> test-writer (skill 2) -> run tests -> "
           "fix -> run the same tests again. For the homework the fix is done by the bug-fixer (skill 3).", "",
           "A test is **good** when it fails on the original code and passes on the fixed code.", "",
           "## Summary", "",
           "| File | Functions | Bug reports | Tests | Fail before fix | Pass after fix | Good tests | Fixed by |",
           "|---|---|---|---|---|---|---|---|"]
    for r in results:
        fail = sum(x["before"] in ("FAILED", "ERROR") for x in r["rows"])
        ok = sum(x["after"] == "PASSED" for x in r["rows"])
        out.append(f"| {r['file']} | {r['functions']} | {r['reports']} | {r['tests']} | {fail}/{r['tests']} "
                   f"| {ok}/{r['tests']} | {r['good']}/{r['tests']} | {r.get('fixed_by', '')} |")
    for r in results:
        out += ["", f"## {r['file']}", "",
                "| # | Function | Level | Line | Bug (from the report) | Test | Before fix | After fix | Good |",
                "|---|---|---|---|---|---|---|---|---|"]
        for x in r["rows"]:
            out.append(f"| {x['report']} | `{x['function']}` | {x['level']} | {x['line']} | {_short(x['problem'])} "
                       f"| `{x['test']}` | {x['before']} | {x['after']} | {'yes' if x['good'] else 'NO'} |")
    with open(path, "w") as f:
        f.write("\n".join(out) + "\n")
    print("\n".join(out))
    return check(f"report saved in {path}", True)
