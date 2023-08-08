# 대입 연산자
# += : 변수에 값을 거하여 할당하는 대입 연산자. 변수의 현재 값과 오른쪽 값을 더하여 왼쪽 변수에 할당
numA = 5
numA += 3  # numA = numA+3
# In the end, numA is 8

# -= : 변수에 값을 빼서 할당하는 대입 연산자. 변수의 현재 값에서 오른쪽의 값을 뼤서 왼쪽 변수에 할당
numB = 10
numB -= 4  # numB = numB-4
# In the end, numB is 6

# *= : 변수에 값을 곱하여 할당하는 대입 연산자. 변수의 현재 값과 오른쪽 값을 곱하여 왼쪽 변수에 할장
numC = 3
numC *= 2  # numC = numC*2
# In the end, numC is 6

# 연산자의 우선 순위
numD = 5
numE = 3

result_1 = numD + numE * 2
result_2 = (numD + numE) * 2
result_3 = numD + numE ** 2
result_4 = (numD + numE) ** 2

print(f'{numD} + {numE} * 2 = {result_1}')
print(f'({numD} + {numE}) * 2 = {result_2}')
print(f'{numD} + {numE} ** 2 = {result_3}')
print(f'({numD} + {numE}) ** 2 = {result_4}')


# 조건문
# case 1
temp1 = True
temp2 = False
temp3 = False

if temp1 and temp2 or temp3:
    print("Ran inside if")
elif temp1 and temp2 and temp3:
    print("Ran inside elif")
else:
    print("Ran inside else")

# case 2
x = 10

if x > 0:
    print("x는 양수입니다")
elif x < 0:
    print("x는 음수입니다")
else:
    print("x는 0입니다")

# case 3
score = int(input("Enter you test score:\n"))

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Grade F")

# for 문
list_month = list(range(1, 13))

print('반복시작')
for _month in list_month:
    print(f'{_month}월')
print('반복종료')


# while 문
i = 0
while i <= 5:
    print(f'i의 현재값은 {i}')
    i += 1


break_cnt = 0
while True:
    if break_cnt == 99:
        break
    print(f'Currently, the break_cnt is {break_cnt}')
    break_cnt += 1

print("1부터 10까지의 짝수를 표시합니다")

for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i}")
    elif i % 2 != 0:
        continue
    i += 1

"""
# Call function


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


num_a = 3
num_b = 5
result_1 = add(num_a, num_b)
result_2 = multiply(num_a, num_b)
print(result_1)
print(result_2)
"""
