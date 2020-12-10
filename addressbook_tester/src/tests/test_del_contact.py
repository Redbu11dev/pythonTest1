import os
from addressbook_tester.src.models.contact import Contact


def test_add_contact(app):
    if app.contact.count() < 1:
        app.contact.create(Contact(last_name="test"))
    app.contact.delete_first_contact()
