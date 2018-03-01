#!/usr/bin/env python3
""" Tests for phonebook.py

Usage:
    nosetests3 -v --rednose test_phonebook.py
"""

import unittest
from app.phonebook import PhoneBook

class TestPhoneBook(unittest.TestCase):
    """ Test Cases """

    def setUp(self):
        """ Configures fixtures and instantinates PhoneBook class """
        # Init
        self.phonebook = PhoneBook()
        name1 = 'Guido'
        name2 = 'Kendrick Lamar'
        name3 = 'Tupac Amaru Shakur'
        num1 = +254721987654
        num2 = +254721654987
        num3 = +123455689999

    def test_for_empty_dict_on_init(self):
        """ Test that class initializes with an empty phone book """
        self.assertIsInstance(self.phonebook, dict, 'Should Init with empty dict')


# Initialization - Test cases
# 

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