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
        pass
    
    def test_for_empty_dict_on_init(self):
        """ Test that class initializes with an empty phone book """
        pass
    
    def test_add_contact_method_adds_contacts(self):
        """ Test addition of name and number as key value pairs """
        pass
    
    def test_add_contact_method_handles_invalid_values(self):
        """ Test handling of invalid value for number during addition """
        pass

    def test_add_contact_method_handles_invalid_values(self):
        """ Test handling already existing name-number pair """
        pass
    
    def test_view_contact_method_displays_contents(self):
        """ Test dispaly of phone book entries """
        pass
    
    def test_view_contact_method_displays_contents(self):
        """ Test dispaly of notification when phonebook is empty """
        pass

    def test_update_contact_method_makes_required_changes(self):
        """ Test update of name-number pair as required """
        pass

    def test_update_contact_method_reports_changes(self):
        """ Test reporting or update operation success/fail status """
        pass

    def test_delete_contact_method_removes_contact(self):
        """ Test deletion of name-number pair matching name """
        pass
    
    def test_delete_contact_method_reports_changes(self):
        """ Test reporting of delete operation success/fail status """
        pass

if __name__ == '__main__':
    unittest.main()



