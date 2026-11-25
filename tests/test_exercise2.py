import os
import sqlite3
import subprocess

import pytest

import exercise2
from exercise2 import *


# bug report 1
def test_r1_is_passing():
    assert is_passing(5) is True, "Grade 5 should return True as it is 5 or more"


# bug report 2
def test_r2_clamp():
    assert clamp(10, 5, 15) == 10


# bug report 3
def test_r3_is_valid_password():
    assert is_valid_password("abcdefg1") is True, "8 characters with a digit is 'at least 8'"
