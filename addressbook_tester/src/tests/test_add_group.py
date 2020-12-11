from addressbook_tester.src.models.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group("group1", "group1_header", "group1_footer"))
    new_groups = app.group.get_group_list()
    assert len(new_groups) == len(old_groups)+1

# app.session.logout()


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group("", "", ""))
    new_groups = app.group.get_group_list()
    assert len(new_groups) == len(old_groups) + 1
