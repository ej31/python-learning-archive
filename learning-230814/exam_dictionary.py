# 빈 딕셔너리 선언 (생성)
empty_dict = {}

# 일반적인 형태의 딕셔너리
dict_type_1 = {"apple": 1.4, "cherry": 1.5}
print(dict_type_1)

dict_type_2 = {
    "fruit": {
        "apple": {
            "price": 100,
            "quantities": 5
        },
        "cherry": {
            "price": 80,
            "quantities": 100
        },
    },
    "manager": [
        "John Smith",
        "홍길동"
    ],
    "manager_lv": [
        {"admin": 100},
        {"user_grade_1": 50},
        {"user_grade_2": 80},
    ]
}

dict_type_3 = dict(
    fruit=dict(
        apple=dict(
            price=100, quantities=5
        ),
        cherry=dict(
            price=80, quantities=100
        )
    ),
    manager=list(
        ["John Smith", "홍길동"]
    ),
    manager_lv=list(
        [
            dict(admin=100),
            dict(user_grade_1=50),
            dict(user_grade_2=80),
        ]
    )
)

print(dict_type_2)
print(dict_type_3)


def some_method():
    _fruit = dict_type_2["fruit"]
    print(_fruit)
    _fruit_with_get = dict_type_2.get("fruit_____", "키가 없습니다.")
    print(_fruit_with_get)


some_method()


def calculator(v1, v2, operator_str):
    if operator_str == "+":
        return add(v1, v2)
    elif operator_str == "-":
        return sub(v1, v2)


def add(v1, v2):
    return v1 + v2


def sub(v1, v2):
    return v1 - v2


# 값 추가 및 변경하기
dict_type_2 = {
    "fruit": {
        "apple": {
            "price": 100,
            "quantities": 5
        },
        "cherry": {
            "price": 80,
            "quantities": 100
        },
    },
    "manager": [
        "John Smith",
        "홍길동"
    ],
    "manager_lv": [
        {"admin": 100},
        {"user_grade_1": 50},
        {"user_grade_2": 80},
    ]
}

dict_type_2["person_name"] = "이강인"
dict_type_2["person_list"] = [
    "히딩크", "홍명보", "황선홍"
]
dict_type_2["others"] = {
    "flag1": True,
    "flag2": False,
    "flag3": True,
    "any_integer": [1, 2, 3],
}

# dict_type_2["fruit"]["apple"] = {
#     "price": 50,
#     "quantities": 10,
#     "grade": "High"
# }

# del dict_type_2["others"]
# print(dict_type_2)
#
# _pop_item = dict_type_2.pop("fruit")
# print(f"dict_type_2, after pop -- {dict_type_2}")
# print(f"_pop_item -- {_pop_item}")
#
# dict_type_2.clear()
# print(f"dict_type_2, after clear -- {dict_type_2}")

for this_is_key in dict_type_2:
    print(f"dict_type_2, item -- {this_is_key}")

for key, value in dict_type_2.items():
    print(f"dict_type_2, key -- {key}, value -- {value}")

# _keys = dict_type_2["fruit"].keys()
# _values = dict_type_2["fruit"].values()
# print(f"_keys -- {_keys}")
# print(f"_values -- {_values}")

for __key in dict_type_2.keys():
    print(f"_keys -- {__key}")

for __value in dict_type_2.values():
    print(f"__value -- {__value}")

# 딕셔너리 업데이트
fruit_cost_dict_1 = {"apple": 100, "cherry": 50}
fruit_cost_dict_2 = {"apple": 5, "melon": 100}

fruit_cost_dict_1.update(fruit_cost_dict_2)

print(fruit_cost_dict_1)

# 업데이트 대안책으로 in 절을 사용한다.
if "apple" in fruit_cost_dict_1:
    fruit_cost_dict_1["apple"] = 5000

if "grape" not in fruit_cost_dict_1:
    fruit_cost_dict_1["grape"] = 100

print(fruit_cost_dict_1)

# 딕셔너리 언패킹
# for key, value in dict_type_2.items():
#     print(f"dict_type_2, key -- {key}, value -- {value}")
