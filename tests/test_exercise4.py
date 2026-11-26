import os
import sqlite3
import subprocess

import pytest

import exercise4
from exercise4 import *


# bug report 1
def test_r1_hardcoded_admin_password():
    assert "admin123" not in open(exercise4.__file__).read()


# bug report 2
def test_r2_sql_injection_vulnerability():
    # Create an in-memory SQLite database for testing
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (username TEXT, password TEXT)")
    conn.execute("INSERT INTO users (username, password) VALUES ('alice', 'pass123')")
    conn.commit()

    # Test with a SQL injection payload
    malicious_username = "x' OR '1'='1"
    result = find_user(conn, malicious_username)

    # The vulnerable function should return the row for the malicious input
    # which is a SQL injection vulnerability - it should return a row (or crash)
    # but it should not return a row for a malicious input
    assert result is None, f"Expected None for malicious input '{malicious_username}', but got {result}"
