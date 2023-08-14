def sum_and_mul(value1: int, value2: int):
    return (value1 + value2) * 2


v1 = 10
v2 = 20
v3 = sum_and_mul(v1, v2)
v2_1 = 10
v2_2 = 20
v2_3 = sum_and_mul(v2_1, v2_2)
v3_1 = 10
v3_2 = 20
v3_3 = sum_and_mul(v3_1, v3_2)
v4_1 = 10
v4_2 = 20
v4_3 = sum_and_mul(v4_1, v4_2)


# 함수의 정의
def 함수이름(매개변수1, 파라미터2):
    print("함수이름시작입니다.")
    print("함수이름처리중입니다. _1")
    print("함수이름처리중입니다. _2")
    print("함수이름처리중입니다. _3")
    print("함수이름처리중입니다. _4")
    print("함수이름처리중입니다. _5")
    return "END!" + 매개변수1 + 파라미터2


결과 = 함수이름("Hello", "Python!")
print(결과)
