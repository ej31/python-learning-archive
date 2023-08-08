# 값과 식
num_1 = 10
num_2 = 20

num_result_1 = num_1 + num_2
print(f'num_result_1 -- {num_result_1}')

# 논리 연산식
bool_1 = True
bool_2 = False

bool_result_with_and = bool_1 and bool_2
print(bool_result_with_and)

bool_1 = True
bool_2 = False

bool_result_with_or = bool_1 or bool_2
print(bool_result_with_or)

# 조건식
x = 10
y = 5

if x > y:
    print("x가 y보다 큼")
else:
    print("y가 x보다 큼")

print("x가 y보다 큼") if x > y else print("y가 x보다 큼")


# 함수 호출식
def add(v1: int, v2: int):
    print(f"x 값은 {v1}, y값은 {v2}")
    return v1 + v2


def multiply(v1: int, v2: int):
    print(f"x 값은 {v1}, y값은 {v2}")
    return v1 * v2


result_add = add(10, 20)
result_multiply = multiply(20, 30)

print(f"result_add -- {result_add}")
print(f"result_multiply -- {result_multiply}")

# 전통적인 방식의 반복문
# for(int i = 0; someList >= someList.length(); i += 2) { }


# 예제 1: 괄호를 사용하여 우선 순위 변경
result1 = 2 + 3 * 4
result2 = (2 + 3) * 4
print(f"result1 -- {result1}")  # Output: 14 (3 * 4가 먼저 계산됨)
print(f"result2 -- {result2}")  # Output: 20 ((2 + 3)가 먼저 계산됨)

# 예제2: 여러 연산자 함께 사용
x = 5
y = 3
result3 = x + y * 2
result4 = (x + y) * 2
result5 = x + y ** 2
result6 = (x + y) ** 2
print(f"result3 -- {result3}")  # Output: 11 (3 * 2가 먼저 계산됨)
print(f"result4 -- {result4}")  # Output: 16 ((5 + 3)가 먼저 계산됨)
print(f"result5 -- {result5}")  # Output: 14 (3 ** 2가 먼저 계산됨)
print(f"result6 -- {result6}")  # Output: 64 ((5 + 3) ** 2가 먼저 계산됨)

print("*")
print("**")
print("***")
print("****")
print("*****")
