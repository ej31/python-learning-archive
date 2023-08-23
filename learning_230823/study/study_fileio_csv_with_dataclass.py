import csv
import os.path
from dataclasses import dataclass, fields
from enum import Enum


def read_person():
    if os.path.getsize("sample.csv") == 0:
        return None
    with open("sample.csv", "r") as _f:
        _reader = csv.reader(_f, )
        next(_reader)
        for _row in _reader:
            print(_row)


class GenderType(Enum):
    MALE = "male"
    FEMALE = "female"


@dataclass
class Person:
    user_name: str
    age: int
    gender: str
    height: float


def save_person(person_data: Person):
    with open("sample.csv", "a", newline='') as _f:
        _writer = csv.writer(_f)
        if os.path.getsize("sample.csv") == 0:
            _writer.writerow(["UserName", "Age", "Gender", "Height"])

        _writer.writerow([
            person_data.user_name,
            person_data.age,
            person_data.gender,
            person_data.height
        ])


save_person(Person(
    user_name="John Smith",
    age=24,
    gender="Male",
    height=184
))

save_person(Person(
    user_name="John Doe",
    age=80,
    gender="Male",
    height=194
))
