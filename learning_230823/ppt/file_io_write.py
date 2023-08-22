# 파일을 쓰기 모드로 엽니다. 파일이 없으면 새로 생성됩니다.
file = open("example.txt", "w")

# 파일에 문자열을 씁니다.
file.write("Hello, World!\n")
file.write("Welcome to Python File I/O.")

# 파일을 닫습니다.
file.close()
