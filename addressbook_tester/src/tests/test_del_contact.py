import os
from random import randrange

from addressbook_tester.src.models.contact import Contact


def test_add_contact(app):
    if app.contact.count() < 1:
        app.contact.create(Contact(last_name="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    # app.contact.delete_first_contact()
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(new_contacts) == len(old_contacts) - 1
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contacts
