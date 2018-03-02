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
        """ Configure fixtures """
        self.phonebook = PhoneBook()

        self.sample1 = {}
        self.sample2 = {'vlad': 12345}
        self.sample3 = {'Tim': 67890, 'vlad': 12345}
        self.errmsg1 = 'Oops... Invalid Entry'
        self.errmsg2 = 'Oops... Phonebook empty'
        self.errmsg3 = 'Success'

    def test_add_contact_method_adds_contacts(self):
        """ Test addition of name and number as key value pairs """
        self.assertEqual(self.sample2, self.phonebook.add_contact('vlad', 12345))

    def test_add_contact_method_handles_invalid_values(self):
        """ Test handling of invalid value for number during addition """
        self.assertEqual(self.errmsg1, self.phonebook.add_contact('vlad', '12345'))
        
    def test_view_contact_method_displays_contents(self):
        """ Test dispaly of phone book entries """
        self.assertEqual(self.errmsg3, self.phonebook.view_contact())
        
    def test_view_contact_method_displays_contents(self):
        """ Test dispaly of notification when phonebook is empty """
        self.phonebook = PhoneBook()
        self.assertEqual(self.errmsg2, self.phonebook.view_contact())

    # def test_update_contact_method_makes_required_changes(self):
    #     """ Test update of name-number pair as required """
    #     pass

    def test_update_contact_method_reports_changes(self):
        """ Test reporting or update operation success/fail status """
        pass

    def test_delete_contact_method_removes_contact(self):
        """ Test deletion of name-number pair matching name """
        self.assertEqual(self.sample2, self.phonebook.delete_contact('Vlad'))
    
    def test_delete_contact_method_reports_changes(self):
        """ Test reporting of delete operation success status """
        self.assertEqual(self.errmsg2, self.phonebook.delete_contact('Tim'))

if __name__ == '__main__':
    unittest.main()



