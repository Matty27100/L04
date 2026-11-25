import os
import sqlite3
import subprocess

import pytest

import homework
from homework import *


# bug report 1
def test_r1_celsius_to_fahrenheit_boiling_point():
    assert celsius_to_fahrenheit(100) == 212


# bug report 2
def test_r2_is_leap_year_2000():
    assert is_leap_year(2000) is True


# bug report 3
def test_r3_median_unsorted_list():
    numbers = [3, 1, 2]
    assert median(numbers) == 2
    assert numbers == [3, 1, 2], "the list itself must not be changed"


# bug report 4
def test_r4_median_empty_list():
    assert median([]) is None


# bug report 5
def test_r5_binary_search_last_element():
    assert binary_search([1, 3, 5], 5) == 2


# bug report 6
def test_r6_ping_command_injection(no_shell):
    assert ping("example.com; rm -rf ~") is False
    assert not any("rm -rf" in str(call) for call in no_shell), "no command may run for an invalid host"
