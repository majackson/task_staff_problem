#!/usr/bin/env python

import sys
from collections import defaultdict


class CompanyHierarchy:
    def __init__(self):
        self.dict = defaultdict(list)

    def add(self, line):
        managee, manager = line.split(" ")
        self.dict[managee].append(manager)

    def length(self):
        return len(self.dict)

    def keys(self):
        return self.dict.keys()


def read_file(input_file):
    """
    Read input file, into key, value pairs.
    """
    company = CompanyHierarchy()
    with open(input_file, "r") as infile:
        for line in infile:
            company.add(line)

    return company

if __name__ == "__main__":
    company = read_file(sys.argv[1])
    first_employee = sys.argv[2]
    second_employee = sys.argv[3]
