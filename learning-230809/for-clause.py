list_month = list(range(1, 13))

month = 99
for _month in list_month:
    # print("반복 시작")
    # print(f"현재 몇월인가요 -- {_month}")
    # print("반복 종료")
    pass

just_txt = "HelloWorld!"

for txt in just_txt:
    print(txt)

## while 문

i = 0
while i <= 5:
    print(f"i의 현재 값은.. {i}")
    i += 1

break_cnt = 0
while True:

    if break_cnt > 5:
        break
    else:
        break_cnt += 1

    if break_cnt == 3:
        print("건너뛸께요!")
        continue
    print(f"현재 break_cnt 값은 ... {break_cnt}")

print("while을 빠져 나왔어요!")
print("while을 빠져 나왔어요!")
print("while을 빠져 나왔어요!")
