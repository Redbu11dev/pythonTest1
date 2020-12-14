import os
from addressbook_tester.src.models.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
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
                       "8(800)2000600",
                       "2000000",
                       "2111111",
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
                       None,  # "group1"
                       "addr2",
                       "+9999999",
                       "some notes"
                       )
    app.contact.create(contact1)
    app.contact.return_to_contacts_page()
    # app.contact.verify_account_created(contact1)
    assert app.contact.count() == len(old_contacts) + 1
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact1)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

