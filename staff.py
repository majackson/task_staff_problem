#!/usr/bin/env python

import sys
from collections import defaultdict


class CompanyHierarchy:
    def __init__(self):
        self.manager_dict = defaultdict(list)
        self.managee_dict = defaultdict(list)

    def add(self, line):
        line = line.replace("\n", "")
        managee, manager = line.split(" ")

        self.manager_dict[managee].append(manager)

        self.managee_dict[manager].append(managee)

        # Resolve managers
        if managee in self.managee_dict.keys():
            for those_managed in self.managee_dict[managee]:
                self.manager_dict[those_managed].append(manager)


    def length(self):
        return len(self.manager_dict)

    def keys(self):
        return self.manager_dict.keys()


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

    first_employee_managers = company.manager_dict[first_employee]
    second_employee_managers = company.manager_dict[second_employee]

    # Preserve Order of intersection
    common_managers = [i for i in first_employee_managers if i in second_employee_managers]
    if len(common_managers)>0:
        print common_managers[0]
