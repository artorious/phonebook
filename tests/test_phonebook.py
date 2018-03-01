#!/usr/bin/env python3
""" Tests for phonebook.py

Usage:
    nosetests3 -v --rednose test_phonebook.py
"""

import unittest
from phonebook import PhoneBook

class TestPhoneBook(unittest.TestCase):
    pass

# Initialization - Test cases
# test inits an empty phone book (dict)

# Addition - Test cases
# test adds a name and number as key value pairs
# test num is int, custom msg if not
# test name is str, custom msg if not

# Views - Test cases
# test dispalys name (key) and associated number
# test custom msg if empty
# test dispalys all contacts when called without param name


# Update - Test cases
# test updates key:value pair matching name (key)
# test custom msg if name not found
# test custom msg before overwriting

# Delete - Test cases
# test deletes key:value pair matching name (key)
# test custom msg if successful
# test custom msg if name not found









if __name__ == '__main__':
    unittest.main()