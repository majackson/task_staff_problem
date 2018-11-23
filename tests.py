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


def test_create_dicts():
    lines = [
        "Adam Bob",
        "Andrea Bob",
        "Aaron Brenda",
        "Aisha Brenda",
        "Brenda Chris",
        "Bob Chris",
    ]
    company = CompanyHierarchy()
    for line in lines:
        company.add(line)
    assert company.manager_length() == 6
    for name in ["Andrea", "Bob", "Aaron", "Brenda", "Aisha"]:
        assert name in company.manager_keys()
    assert company.managee_length() == 3
    for name in ["Chris", "Bob", "Brenda"]:
        assert name in company.managee_keys()
