#!/usr/bin/env python3
"""A simple Phone book program.

Features:
    Add contacts
    Update contacts
    Delete contacts
    View contacts
"""

class PhoneBook(object):
    """ Subclassed to dict, holds methods that manage a phone book """
    def __init__(self):
        """ Init with an empty dict """
        pass

    def add_contact(self, name, number):
        """ Adds a contact to phonebook """
        pass
    
    def view_contact(self, name=False):
        """ View contacts in phone book """
        # print(self.phonebook)
        pass
    
    def update_contact(self, name, number):
        """ Update contacts in phonebook """
        pass
    
    def delete_contact(self, name):
        """ Delete a contact from phone book """
        pass


def main():
    pass

if __name__ == '__main__':
    main()