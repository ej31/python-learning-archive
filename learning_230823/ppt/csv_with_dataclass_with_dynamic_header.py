from dataclasses import dataclass, fields
import csv


@dataclass
class Person:
    Name: str  # 이 속성 값이 (Name) CSV 헤더로 쓰인다.
    Age: int  # CSV에는 헤더 값이 포함이 될 수도 있고 아닐 수도 있는 점 참고
    City: str


people = [
    Person("Alice", 30, "New York"),
    Person("Bob", 25, "Los Angeles"),
    Person("Charlie", 35, "Chicago"),
]

# CSV 파일에 저장
with open("people.csv", "w", newline='') as file:
    writer = csv.writer(file)

    # 헤더 작성 (하드코딩 없이 필드 이름 사용)
    headers = [field.name for field in fields(Person)]
    writer.writerow(headers)

    # 각 Person 객체의 데이터를 CSV 파일에 작성
    for person in people:
        writer.writerow([person.Name, person.Age, person.City])
