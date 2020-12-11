from addressbook_tester.src.models.group import Group


def test_modify_group_name(app):
    if app.group.count() < 1:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="New Group"))
    new_groups = app.group.get_group_list()
    assert len(new_groups) == len(old_groups)


def test_modify_group_header(app):
    if app.group.count() < 1:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="New Header"))
    new_groups = app.group.get_group_list()
    assert len(new_groups) == len(old_groups)
