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
        self.phonebook = {}

    def add_contact(self, name, number):
        """ Adds a contact to phonebook """
        if isinstance(number, int):
            self.phonebook[name] = number
            return self.phonebook
        else:
            return 'Oops... Invalid Entry'

    def view_contact(self, name=False):
        """ View contacts in phone book """
        return
    
    def update_contact(self, name, number):
        """ Update contacts in phonebook """
        return
    
    def delete_contact(self, name):
        """ Delete a contact from phone book """
        return


def main():
    pass

if __name__ == '__main__':
    main()