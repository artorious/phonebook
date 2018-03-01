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
        self.playbook = PhoneBook()
    
    
    def test_for_empty_dict_on_init(self):
        """ Test that class initializes with an empty phone book """
        self.assertIsInstance(
            self.playbook, dict, 'Should Init with empty dict')
    
    def test_add_contact_method_adds_a_contact(self):
        result1 = {'Guido': +254721987654}
        self.assertEqual(
            result1, self.playbook.add_contact('Guido', 254721987654))
    
    def test_view_contact_method_displays_contents(self):
        result2 = {'van': +254721654987, 'Guido': +254721987654}
        result3 = {'van': +254721654987}

        self.assertEqual(result2, self.playbook.view_contact())
        self.assertEqual(result3, self.playbook.view_contact('van'))

    def test_delete_contact_method(self):
        result4 = {'van': +254721654987}
        self.playbook = {'van': +254721654987, 'Guido': +254721987654}
        self.assertDictEqual(result4, self.playbook.delete_contact('Guido'))

    def test_update_contact_method(self):
        result4 = {'van': +254721654987}
        self.assertEqual(
            result4, self.playbook.update_contact('van', +254721654987))

        

if __name__ == '__main__':
    unittest.main()


        

