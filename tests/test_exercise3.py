import os
import sqlite3
import subprocess

import pytest

import exercise3
from exercise3 import *


# bug report 1
def test_r1_average_empty_list():
    assert average([]) == 0


# bug report 2
def test_r2_first_word():
    assert first_word("hello world") == "hello"
    assert first_word("  ") == ""
    assert first_word("") == ""
    assert first_word("   hello") == "hello"
    assert first_word("world") == "world"


# bug report 3
def test_r3_percent():
    assert percent(5, 10) == 50.0
    assert percent(0, 10) == 0.0
    assert percent(0, 0) == 0
    assert percent(-5, 10) == -50.0
    assert percent(5, 0) == 0
    assert percent(3.5, 10) == 35.0
    assert percent(1, 3) == 33.333333333333336
