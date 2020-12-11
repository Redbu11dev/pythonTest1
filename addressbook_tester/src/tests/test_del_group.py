from addressbook_tester.src.models.group import Group


def test_del_group(app):
    if app.group.count() < 1:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(new_groups) == len(old_groups) - 1