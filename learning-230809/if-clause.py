## 조건문
# case. 1
조건식1 = True
조건식2 = True
조건식3 = True

if 조건식1 and 조건식2 or 조건식3:
    print("if문 안쪽을 실행했어요")
elif 조건식1 and 조건식2 and 조건식3:
    print("elif문 안쪽을 실행했어요")
else:
    print("else문 안쪽을 실행했어요")

# case. 2
x = 0
if x > 0:
    print("x는 양수")
elif x < 0:
    print("x는 음수")
else:
    print("x는 0!")

# case. 3
score = int(input("시험점수 입력하세요\n"))

if score >= 90:
    print("학점 A")
elif score >= 80:
    print("학점 B")
elif score >= 70:
    print("학점 C")
else:
    print("제적. 나가라")
