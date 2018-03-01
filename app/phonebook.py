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
        self.phonebook = {}

    def add_contact(self, name, number=None):
        """ Add a contact """
        self.phonebook[name] = number
        return self.phonebook
    
    def view_contact(self, name=False):
        """ View contacts """
        print(self.phonebook)
    
    def update_contact(self, name, number):
        """ Update contacts """
        self.phonebook[name] = number
        return self.phonebook
    
    def delete_contact(self, name):
        """ Delete a contact """
        self.phonebook.pop(name, 'Name not found')


def main():
    result2 = {'van': +254721654987, 'Guido': +254721987654}
    result3 = {'van': +254721654987}

    result2.view_contact()

if __name__ == '__main__':
    main()