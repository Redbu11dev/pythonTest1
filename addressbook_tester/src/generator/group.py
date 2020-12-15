import jsonpickle
import os

from addressbook_tester.src.models.group import Group
import pytest
import random
import string
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    # print help information and exit:
    # print(err)  # will print something like "option -a not recognized"
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

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


constant = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]

testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10).strip().replace("/  +/g", " "),
          header=random_string("header", 20).strip().replace("/  +/g", " "),
          footer=random_string("footer", 20).strip().replace("/  +/g", " "))
    for i in range(n)
]

# file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/groups.json")
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    # out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
