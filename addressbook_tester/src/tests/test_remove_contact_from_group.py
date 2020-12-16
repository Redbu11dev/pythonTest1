import random

from addressbook_tester.src.models.contact import Contact
from addressbook_tester.src.models.group import Group


def test_remove_contact_from_group(app, db, orm_db):
    group = Group(id="179")
    old_contacts_in_group = orm_db.get_contacts_in_group(group)
    contact = random.choice(old_contacts_in_group)
    app.contact.remove_contact_from_group(contact.id, group.id)
    new_contacts_in_group = orm_db.get_contacts_in_group(group)
    for new_contact in new_contacts_in_group:
        if new_contact.id == contact.id:
            raise AssertionError("contact still exists in the group")
    else:
        pass  # all good
