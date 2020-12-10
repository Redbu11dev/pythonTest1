import os
from addressbook_tester.src.models.contact import Contact


def test_add_contact(app):
    app.contact.delete_first_contact()
