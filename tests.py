import pytest
import os
import subprocess

from staff import *

COMMAND = "./staff.py"
INPUT = "staff.input"


def test_read_file():
    output = subprocess.check_output([COMMAND, INPUT, "John", "Jane"])
    assert output == "John\n"
