#!/usr/bin/env python

import sys

def read_file(input_file):
    """
    Read input file, into key, value pairs.
    """
    with open(input_file, "r") as infile:
        for line in infile:
            managee_name, manager_name = line.split(" ")
            print managee_name, manager_name

if __name__ == "__main__":
    read_file(sys.argv[1])
