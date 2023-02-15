from app.Server import Server
from app.modules.core_database import Connector
from app.modules.api import People

import uuid
import random 

import time

from random import choice
from names import get_first_name, get_last_name

people_api = People()
# people_api.add_person()

middle_names = [
    "Olegovich",
    "Nikitin",
    "Grigorievich",
    "Yourievich"
]

def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)

def generate_uuid():
    return uuid.uuid4().hex

def generate_average_mark():
    return random.randrange(2, 5) + random.randrange(0, 10) / 10

def generate_birthday():
    return random_date("1/1/2000 1:30 PM", "1/1/2005 4:50 AM", random.random())

def generate_name():
    return [get_first_name(gender="male") , get_last_name(), choice(middle_names)]

# def add_user():
#     people_api.add_person(

#     )

# print(generate_uuid())
# print(generate_average_mark())
# print(generate_birthday())

# name, surname, middle_name = generate_name()


# people_api.add_person(name, surname, middle_name,
#     generate_birthday(),
#     generate_average_mark(),
#     generate_uuid()
# )

# print(generate_name())
# print(generate_name())

serv = Server()
serv.init()


# """

#     TEST one

# """

# def decoration_factory(operation):
#     def decor(func):
    
#         def wrapper():
#             func()
#             print(operation)
#             func()


#         return wrapper
#     return decor

# @decoration_factory(111)
# def test():
#     print(1)

# test()