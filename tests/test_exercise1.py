import os
import sqlite3
import subprocess

import pytest

import exercise1
from exercise1 import *


# bug report 1
def test_r1_is_even_docstring():
    """Test that is_even returns True for even numbers and False for odd numbers."""
    assert is_even(4) is True  # even number
    assert is_even(3) is False  # odd number
    assert is_even(0) is True  # zero is even
    assert is_even(-2) is True  # negative even number
    assert is_even(-3) is False  # negative odd number


# bug report 2
def test_r2_rectangle_area_docstring():
    """Test that the rectangle_area docstring correctly describes the function."""
    assert rectangle_area.__doc__ == "Returns the area of a rectangle given its width and height (in square units)."


# bug report 3
def test_r3_double():
    assert double(4.5) == 9.0, "double(4.5) should return 9.0"
