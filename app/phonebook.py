#!/usr/bin/env python3
"""A simple Phone book program.

Features:
    Add contacts
    Update contacts
    Delete contacts
    View contacts
"""

class PhoneBook(dict):
    """ Subclassed to dict, holds methods that manage a phone book """
    def __init__(self):
        """ Init with an empty dict """
        phonebook = {}

    def add_contact(self, name, number=None):
        """ Add a contact """
        pass
    
    def view_contact(self, name=False):
        """ View contacts """
        pass
    
    def update_contact(self, name):
        """ Update contacts """
        pass
    
    def delete_contact(self, name):
        """ Delete a contact """
        pass


def main():
    pass

if __name__ == '__main__':
    main()