#!/usr/bin/env python

import sys
from collections import defaultdict


class CompanyHierarchy:
    """
    Simple class to manage the managee-manager relations of a
    Company
    """
    def __init__(self):
        self.manager_dict = defaultdict(list)
        self.managee_dict = defaultdict(list)

    def add(self, line):
        line = line.replace("\n", "")
        managee, manager = line.split(" ")

        self.manager_dict[managee].append(manager)

        self.managee_dict[manager].append(managee)

        # Check if a Managee is also a Manager. If True,
        if managee in self.managee_dict.keys():

            # for each employee that the Managee is managing,
            for those_managed in self.managee_dict[managee]:

                # add the Manager as their Manager
                self.manager_dict[those_managed].append(manager)


    def manager_length(self):
        return len(self.manager_dict)

    def manager_keys(self):
        return self.manager_dict.keys()

    def managee_length(self):
        return len(self.managee_dict)

    def managee_keys(self):
        return self.managee_dict.keys()

    def common_managers(self, first_employee, second_employee):
        """
        Return an ordered list of common managers for two employees.
        """

        common_managers = []

        first_employee_managers = self.manager_dict[first_employee]
        second_employee_managers = self.manager_dict[second_employee]

        # Preserve Order of intersection
        common_managers = [i for i in first_employee_managers if i in second_employee_managers]

        return common_managers

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

    common_managers = company.common_managers(first_employee, second_employee)
    if len(common_managers)>0:
        print common_managers[0]
    else:
        print ""
