from addressbook_tester.src.models.group import Group
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
# constant = [
#     Group(name="name1", header="header1", footer="footer1"),
#     Group(name="name2", header="header2", footer="footer2")
# ]
#
# testdata = [Group(name="", header="", footer="")] + [
#         Group(name=random_string("name", 10).strip().replace("/  +/g", " "),
#               header=random_string("header", 20).strip().replace("/  +/g", " "),
#               footer=random_string("footer", 20).strip().replace("/  +/g", " "))
#         for i in range(5)
#     ]

testdata = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]