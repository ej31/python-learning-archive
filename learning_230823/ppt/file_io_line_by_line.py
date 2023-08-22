with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip()을 사용하여 줄바꿈 문자를 제거
