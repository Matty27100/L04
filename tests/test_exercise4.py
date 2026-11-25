import os
import sqlite3
import subprocess

import pytest

import exercise4
from exercise4 import *


# bug report 1
def test_r1_no_hardcoded_admin_password():
    assert "admin123" not in open(exercise4.__file__).read()


# bug report 2
def test_r2_find_user_sql_injection():
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE users (username TEXT, email TEXT)")
    db.execute("INSERT INTO users VALUES ('ana', 'ana@mail.com')")
    assert find_user(db, "x' OR '1'='1") is None
    assert find_user(db, "ana") == ("ana", "ana@mail.com")
