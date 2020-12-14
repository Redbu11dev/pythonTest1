import os
import pytest
import random
import string
from addressbook_tester.src.models.contact import Contact

def random_string(prefix, maxlen):
    # Не будут группы создаваться с тем же именем, если есть двойные пробелы, ><, возможно ещё что-то.
    # Не надо тут так делать.
    # symbols = string.ascii_letters+string.digits+string.punctuation+" "*10
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
        # Group(name=random_string("name", 10).strip().replace("/  +/g", " "),
        #       header=random_string("header", 20).strip().replace("/  +/g", " "),
        #       footer=random_string("footer", 20).strip().replace("/  +/g", " "))
        Contact(first_name=random_string("first_name", 10).strip().replace("/  +/g", " "),
                       middle_name="Middle name",
                       last_name=random_string("last_name", 10).strip().replace("/  +/g", " "),
                       nickname="Nickname",
                       photo_path=None,
                       title="Title",
                       company="Company",
                       address=random_string("address", 10).strip().replace("/  +/g", " "),
                       home_phone_number="222-22-22",
                       mobile_phone_number="8(800)2000600",
                       work_phone_number="2000000",
                       fax_number="2111111",
                       email_1="email1@mail.com",
                       email_2="email2@mail.com",
                       email_3="email3@mail.com",
                       homepage="www.google.com",
                       birthday_day="1",
                       birthday_month="January",
                       birthday_year="1990",
                       anniversary_day="1",
                       anniversary_month="February",
                       anniversary_year="1867",
                       group_name=None,  # "group1"
                       address_2="addr2",
                       phone_2="+9999999",
                       notes="some notes"
                       )
        for i in range(5)
    ]

@pytest.mark.parametrize("contact1", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact1):
    old_contacts = app.contact.get_contact_list()
    # image_path = os.path.join(os.path.dirname(__file__), '../resources/images/grapefruit-slice-332-332.jpg').replace("/", "\\")
    app.contact.create(contact1)
    app.contact.return_to_contacts_page()
    # app.contact.verify_account_created(contact1)
    assert app.contact.count() == len(old_contacts) + 1
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact1)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

