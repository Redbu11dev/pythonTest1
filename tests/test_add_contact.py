import os

from application import Application
from models.contact import Contact
import unittest


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_contact(self):
        self.app.login("admin", "secret")
        image_path = os.path.join(os.path.dirname(__file__), '../images/grapefruit-slice-332-332.jpg').replace("/", "\\")
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
        self.app.create_contact(contact1)
        self.app.return_to_contacts_page()
        self.app.verify_account_created(self, contact1)
        self.app.logout()

    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
