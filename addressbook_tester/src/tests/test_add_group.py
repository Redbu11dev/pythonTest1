# from addressbook_tester.src.models.group import Group
# import pytest
# import random
# import string
#
#
# def random_string(prefix, maxlen):
#     # Не будут группы создаваться с тем же именем, если есть двойные пробелы, ><, возможно ещё что-то.
#     # Не надо тут так делать.
#     # symbols = string.ascii_letters+string.digits+string.punctuation+" "*10
#     symbols = string.ascii_letters + string.digits + " " * 10
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
# # testdata = [
# #         Group(name=name, header=header, footer=footer)
# #         for name in ["", random_string("name", 10)]
# #         for header in ["", random_string("header", 20)]
# #         for footer in ["", random_string("footer", 20)]
# #     ]
#
# testdata = [Group(name="", header="", footer="")] + [
#         Group(name=random_string("name", 10).strip().replace("/  +/g", " "),
#               header=random_string("header", 20).strip().replace("/  +/g", " "),
#               footer=random_string("footer", 20).strip().replace("/  +/g", " "))
#         for i in range(5)
#     ]

import pytest
from addressbook_tester.src.models.group import Group
# from addressbook_tester.src.data.add_group import testdata
# from addressbook_tester.src.data.groups import constant as testdata

# @pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, db, json_groups):
    group = json_groups
    # old_groups = app.group.get_group_list()
    old_groups = db.get_group_list()
    app.group.create(group)
    assert app.group.count() == len(old_groups) + 1
    # new_groups = app.group.get_group_list()
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
