# Known Issue!!! <-- IMPORTANT

test_blif.py is intended to test **the LOGIC** and **NOT the SYNTAXT** of your project, so it assumes your project being "syntactically correct". 
Therefore make sure that SIS successfully parse and load your script before running test_blif.py
**In case of SIS gives errors at loading time, test_blif.py will gracefully fail giving you the feeling of "green lights", but the project actually doesn't even "compile"!!!**


# test-blif
A tool designed to automate the testing of sequential circuits written for .blif files for [SIS](https://ptolemy.berkeley.edu/projects/embedded/pubs/downloads/sis/index.htm).
A legacy tool developed by Berkeley and still used by UniVR, Università di Verona, for the course of the IT department "Architettura degli Elaboratori" held by Prof. Franco Fummi.


# Install:

    sudo -H pip3 install testblif

*currently only python3 is supported*

# Usage

Print this help:  
$ test_blif.py -h

Print this full help:  
$ test_blif.py --help

Run tests of single blif file:  
$ test_blif.py filename.blif

Run tests on all .blif in the folder:  
$ test_blif.py [-a|--all]


# Tests

In order to add test to you blif file you can add comments in the following format directly in the file you want to test, suggested after the last ".end"
Multiple test can be added to a single .blif to address multiple scenarios. Each test runs independently from the others in new instance of SIS.

## Test format

    #?# [Test_name_or_description]
    # <inputs>|<expected_outputs>
    # <inputs>|<expected_outputs>
    # <inputs>|<expected_outputs>
    #!#

## Test examples

    #?# Truth table OR
    # 00 | 0
    # 01 | 1
    # 10 | 1
    # 11 | 1
    #!#

    #?# 2 bit counter with overflow INC | OUT OVER
    # 1 | 00 0
    # 1 | 01 0
    # 1 | 10 0
    # 0 | 10 0
    # 1 | 11 0
    # 1 | 00 1
    #!#

## File example

    .model MUX4
    .inputs S A3 A2 A1 A0 B3 B2 B1 B0
    .outputs OUT3 OUT2 OUT1 OUT0

    .names S A3 B3 OUT3
    11- 1
    0-1 1

    .names S A2 B2 OUT2
    11- 1
    0-1 1

    .names S A1 B1 OUT1
    11- 1
    0-1 1

    .names S A0 B0 OUT0
    11- 1
    0-1 1

    .end


    #?# MUX4: S A B | OUT
    # 0 1110 0010 | 0010
    # 1 1110 1010 | 1110
    # 0 0101 0110 | 1110
    # 1 0110 0010 | 0110
    # 0 1010 0010 | 0010
    #!#

    #?# MUX4: S A B | OUT
    # 0 0101 0110 | 1110
    # 0 0110 0010 | 0010
    # 0 1010 0010 | 0010
    # 1 1010 0010 | 1010
    # 1 1110 1010 | 1110
    #!#
    
    
