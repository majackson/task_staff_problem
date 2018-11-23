import pytest
import os
import subprocess

from staff import *

COMMAND = "./staff.py"
INPUT = "staff.input"


def test_script():
    output = subprocess.check_output([COMMAND, INPUT, "Adam", "Andrea"])
    assert output == "Bob\n"

    output = subprocess.check_output([COMMAND, INPUT, "Adam", "Aisha"])
    assert output == "Chris\n"

    output = subprocess.check_output([COMMAND, INPUT, "Brenda", "Andrea"])
    assert output == "Chris\n"


