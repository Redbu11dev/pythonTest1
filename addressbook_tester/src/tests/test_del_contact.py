import os
import random
from random import randrange

from addressbook_tester.src.models.contact import Contact


# def test_add_contact(app):
#     if app.contact.count() < 1:
#         app.contact.create(Contact(last_name="test"))
#     old_contacts = app.contact.get_contact_list()
#     index = randrange(len(old_contacts))
#     # app.contact.delete_first_contact()
#     app.contact.delete_contact_by_index(index)
#     new_contacts = app.contact.get_contact_list()
#     assert len(new_contacts) == len(old_contacts) - 1
#     old_contacts[index:index + 1] = []
#     assert old_contacts == new_contacts

def test_del_contact(app, db, check_ui):
    if len(db.get_contact_list()) < 1:
        app.contact.create(Contact(last_name="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(new_contacts) == len(old_contacts) - 1
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
