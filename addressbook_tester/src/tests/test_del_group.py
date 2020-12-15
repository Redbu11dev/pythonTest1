import random
from random import randrange

from addressbook_tester.src.models.group import Group


def test_delete_some_group(app, db):
    # if app.group.count() < 1:
    #     app.group.create(Group(name="test"))
    # old_groups = app.group.get_group_list()
    if len(db.get_group_list()) < 1:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    # new_groups = app.group.get_group_list()
    new_groups = db.get_group_list()
    assert len(new_groups) == len(old_groups) - 1
    old_groups.remove(group)
    assert old_groups == new_groups
