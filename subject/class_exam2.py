class ClassName:
    def __init__(self, parameter1, parameter2):
        # 초기화 메서드 (생성자)
        # 객체가 생성될 때 자동으로 호출되며, 속성 초기화 등의 작업을 수행
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        # ...

    def method1(self, parameter):
        # 메서드 정의
        # 클래스의 기능을 나타내는 작업을 수행
        # self는 메서드가 호출되는 객체 자체를 나타냄
        pass

    def method2(self, parameter):
        # 다른 메서드 정의
        # self와 parameter를 활용하여 작업 수행
        pass


class Car:
    def __init__(self, color, model):
        self.color = color  # 색상
        self.model = model  # 모델

    def display_info(self):  # 정보 출력 메소드
        return f"{self.color} 색의 {self.model} 모델입니다."


# 인스턴스 생성
my_car = Car("red", "Tesla")

# 출력
print(my_car.display_info())
