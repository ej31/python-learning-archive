# 파일을 읽기 모드로 엽니다.
file = open("example.txt", "r")

# 파일의 내용을 읽어 출력합니다.
content = file.read()
print(content)  # Hello, World! Welcome to Python File I/O.

# 파일을 닫습니다.
file.close()
