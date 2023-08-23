from dataclasses import dataclass


class personnotdataclass:
    name: str = "123123"


@dataclass
class PersonDto:
    name: str
    age: int
    is_man: bool  # true: 남자
    height: int


def make_hong_gil_dong():
    return PersonDto(name="홍길동", age=50, is_man=true, height=180)


def some_function(v1, v2, list_1):
    # _v1 = v1
    # _v2 = v2
    list_2 = list_1.copy()  # list_1 변수의 메모리 참조 주소만 넘긴다.
    list_2.append("hello! everyone!")
    v1 = "c"
    v2 = "d"

    return v1, v2


this_is_a = "a"
this_is_b = "b"
this_is_list = [0, 1, 2, 3, 4, 5, 6]
some_function(this_is_a, this_is_b, this_is_list)
print(this_is_list)
