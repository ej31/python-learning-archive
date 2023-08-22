# 파일 쓰기
with open("example.txt", "w") as file:
    file.write("Using with statement for file I/O.")

# 파일 읽기
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # Using with statement for file I/O.
