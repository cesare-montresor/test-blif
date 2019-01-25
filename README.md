# test-blif
A tool to simplyfy the circuit testing written for .blif files in SIS

# Usage

Print this help:
$ test_blif.py -h

Print this full help:
$ test_blif.py --help

Run tests of single blif file:
$ test_blif.py filename.blif

Run tests on all .blif in the folder:
$ test_blif.py [-a|--all]

# Requirments:
python3

    sudo -H pip3 install prettytable ptable

# Tests

In order to add test to you blif file you can add comments in the following format directly in the file you want to test, suggested after the last ".end"
Multiple test can be added to a single .blif to address multiple scenarios. Each test runs independently from the others in new instance of SIS.

## Test format:

    #?# [Test_name_or_description]
    # <inputs>|<expected_outputs>
    # <inputs>|<expected_outputs>
    # <inputs>|<expected_outputs>
    #!#

## Examples:

    #?# Truth table OR
    # 00 | 0
    # 01 | 1
    # 10 | 1
    # 11 | 1
    #!#

    #?# 2 bit counter with overflow INC | C1 C0 COUT
    # 1 | 00 0
    # 1 | 01 0
    # 1 | 10 0
    # 1 | 11 0
    # 1 | 00 1
    #!#

