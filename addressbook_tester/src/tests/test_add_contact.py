import os
import pytest

from addressbook_tester.src.application import Application
from addressbook_tester.src.models.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login("admin", "secret")
    image_path = os.path.join(os.path.dirname(__file__), '../resources/images/grapefruit-slice-332-332.jpg').replace("/", "\\")
    contact1 = Contact("First name",
                       "Middle name",
                       "Ivanov",
                       "Nickname",
                       image_path,
                       "Title",
                       "Company",
                       "Address",
                       "222-22-22",
                       "88002000600",
                       "200-00-00",
                       "211-11-11",
                       "email1@mail.com",
                       "email2@mail.com",
                       "email3@mail.com",
                       "www.google.com",
                       "1",
                       "January",
                       "1990",
                       "1",
                       "February",
                       "1867",
                       "",  # "group1"
                       "addr2",
                       "Home something",
                       "some notes"
                       )
    app.create_contact(contact1)
    app.return_to_contacts_page()
    app.verify_account_created(contact1)
    app.session.logout()
