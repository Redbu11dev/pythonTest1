import os
from addressbook_tester.src.models.contact import Contact


def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.delete_first_contact()
    app.session.logout()
