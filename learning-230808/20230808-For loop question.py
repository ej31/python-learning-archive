# Question 1
print("1부터 10까지의 짝수를 표시합니다")

for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i}")
    elif i % 2 != 0:
        continue
    i += 1
print('\n')

# Question 2
print("1부터 10까지의 짝수를 표시합니다")

for i in range(2, 11, 2):
    print(i)
print('\n')

# Question 3
print("구구단을 작성해보자")

for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i * j}', end='\t')
    print()
print('\n')

# Question 4
for i in reversed(range(1, 6)):
    for j in range(i, 6):
        print("*", end='')
    print()
print('\n')

# Question 5
for i in range(1, 6):
    for j in reversed(range(i, 6)):
        print("*", end='')
    print()
print('\n')

# Question 6 (정삼각형)

# Question 7 (역삼각형)

# Question 8 (오각성)