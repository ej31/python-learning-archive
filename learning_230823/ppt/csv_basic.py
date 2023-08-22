import csv

# CSV 파일 쓰기
with open("example.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 30])
    writer.writerow(["Bob", 25])

# CSV 파일 읽기
with open("example.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # ['Name', 'Age'], ['Alice', 30], ['Bob', 25]
