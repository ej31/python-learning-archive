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

_fruit = dict_type_2["fruit"]
print(_fruit)

_fruit_with_get = dict_type_2.get("fruit_____", "키가 없습니다.")
print(_fruit_with_get)

