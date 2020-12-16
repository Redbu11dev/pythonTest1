import random

from addressbook_tester.src.models.contact import Contact

def test_add_contact_to_group(app, db, orm_db):
    group = random.choice(db.get_group_list())
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.add_contact_to_group(contact.id, group)
    new_contacts_in_group = orm_db.get_contacts_in_group(group)
    for new_contact in new_contacts_in_group:
        if new_contact.id == contact.id:
            assert True
            break
    else:
        raise AssertionError("contact not found")

