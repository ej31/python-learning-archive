from dataclasses import dataclass
import csv


# 데이터를 표현할 클래스 정의
@dataclass
class Person:
    name: str
    age: int
    city: str


# Person 객체의 목록
people = [
    Person("Alice", 30, "New York"),
    Person("Bob", 25, "Los Angeles"),
    Person("Charlie", 35, "Chicago"),
]

# CSV 파일에 저장
with open("people.csv", "w", newline='') as file:
    writer = csv.writer(file)

    # 헤더 작성
    writer.writerow(["Name", "Age", "City"])

    # 각 Person 객체의 데이터를 CSV 파일에 작성
    for person in people:
        writer.writerow([person.name, person.age, person.city])
