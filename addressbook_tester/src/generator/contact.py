import jsonpickle
import os

from addressbook_tester.src.models.contact import Contact
from addressbook_tester.src.models.group import Group
import pytest
import random
import string
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    # print help information and exit:
    # print(err)  # will print something like "option -a not recognized"
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    # Не будут группы создаваться с тем же именем, если есть двойные пробелы, ><, возможно ещё что-то.
    # Не надо тут так делать.
    # symbols = string.ascii_letters+string.digits+string.punctuation+" "*10
    symbols = string.ascii_letters + string.digits + " "# * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# constant = [
#     Contact(name="name1", header="header1", footer="footer1"),
#     Group(name="name2", header="header2", footer="footer2")
# ]

testdata = [
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
        for i in range(n)
    ]

# file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/groups.json")
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    # out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
