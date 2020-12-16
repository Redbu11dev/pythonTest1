# from addressbook_tester.src.helpers.db import DbFixture
#
# db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")
#
# try:
#     contacts = db.get_contact_list()
#     for contact in contacts:
#         print(contact)
#     print(len(contacts))
# finally:
#     db.destroy()

from addressbook_tester.src.helpers.orm import ORMFixture
from addressbook_tester.src.models.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

# try:
#     l = db.get_contact_list()
#     for item in l:
#         print(item)
#     print(len(l))
# finally:
#     pass

try:
    l = db.get_contacts_not_in_group(Group(id="179"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass