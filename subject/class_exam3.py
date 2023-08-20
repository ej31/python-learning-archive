"""클래스 변수는 라디오 방송국의 주파수와 같습니다. 모든 라디오 수신기(인스턴스)가 동일한 주파수(클래스 변수)를 수신합니다. 주파수를 변경하면 모든 수신기에 영향을 미칩니다."""


# 1. 방송국에서 주파수 변경
# 방송국에서 주파수를 변경하면 모든 라디오 수신기에서 변경된 주파수를 수
class BroadcastByRadioType1:
    frequency = "100.1 FM"


radio_1 = BroadcastByRadioType1()
radio_2 = BroadcastByRadioType1()
radio_3 = BroadcastByRadioType1()

print(f"[변경 전] radio_1.frequency -- {radio_1.frequency}")  # 101.5 FM
print(f"[변경 전] radio_2.frequency -- {radio_2.frequency}")  # 101.5 FM
print(f"[변경 전] radio_3.frequency -- {radio_3.frequency}")  # 101.5 FM
print()
BroadcastByRadioType1.frequency = "101.5 FM"  # 클래스에서 직접 변경
print(f"[변경 후] radio_1.frequency -- {radio_1.frequency}")  # 101.5 FM
print(f"[변경 후] radio_2.frequency -- {radio_2.frequency}")  # 101.5 FM
print(f"[변경 후] radio_3.frequency -- {radio_3.frequency}")  # 101.5 FM


# 2. 개별 라디오에서 주파수 변경
# 개별 라디오에서 주파수를 변경하면 해당 라디오만 영향을 받고, 다른 라디오는 영향을 받지 않음
class BroadcastByRadioType2:
    frequency = "100.1 FM"


type2_radio_1 = BroadcastByRadioType2()

type2_radio_2 = BroadcastByRadioType2()
type2_radio_3 = BroadcastByRadioType2()
print(type2_radio_1.frequency)  # 101.5 FM
print(type2_radio_2.frequency)  # 100.1 FM
print(type2_radio_3.frequency)  # 100.1 FM
type2_radio_1.frequency = "101.5 FM"  # 인스턴스 변수 생성

print(type2_radio_1.frequency)  # 101.5 FM
print(type2_radio_2.frequency)  # 100.1 FM
print(type2_radio_3.frequency)  # 100.1 FM


# 3. 방송국 관리자를 통한 주파수 변경
# 방송국 관리자(클래스 메서드)를 통해 주파수를 안전하게 변경할 수 있다.
class BroadcastByRadioType3:
    frequency = "100.1 FM"

    @classmethod
    def set_frequency(cls, frequency):
        cls.frequency = frequency


BroadcastByRadioType3.set_frequency("101.5 FM")

type3_radio_1 = BroadcastByRadioType3()
print(type3_radio_1.frequency)  # 101.5 FM


# 클래스 메서드
class Employee:
    raise_amount = 1.04  # 클래스 변수
    __count = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.__protect_variable = "!"

    @classmethod
    def set_raise_amount(cls, amount):  # 클래스 메서드
        cls.raise_amount = amount  # 클래스 변수를 변경


# 클래스 메서드를 사용하여 클래스 변수를 변경
Employee.set_raise_amount(1.05)

# 클래스 변수가 변경되었음을 확인
print(Employee.raise_amount)  # 출력: 1.05
a = Employee(1, 2, 3)


# 자동차 예제 -- 캡슐화
class Car:
    def __init__(self):
        self.__engine_status = "off"  # 비공개 속성

    def start_engine(self):  # 공개 메서드
        self.__engine_status = "on"
        print("Engine is now on.")

    def stop_engine(self):  # 공개 메서드
        self.__engine_status = "off"
        print("Engine is now off.")


# 객체 생성
my_car = Car()

# 공개 메서드를 통해 엔진 상태 변경
my_car.start_engine()  # 출력: Engine is now on.
my_car.stop_engine()  # 출력: Engine is now off.


# 비공개 속성에 직접 접근하려 하면 오류 발생
# print(my_car.__engine_status)  # AttributeError

# 단일 언더 스코어
class MyClass:
    def __init__(self):
        self._internal_variable = 5

    def _internal_method(self):
        print("This is an internal method.")


# 더블 언더 스코어
class MyClass:
    def __init__(self):
        self.__private_variable = 5

    def __private_method(self):
        print("This is a private method.")


obj = MyClass()

# obj.__private_method()  # AttributeError
# obj.__private_variable  # AttributeError


obj = MyClass()
print(obj._MyClass__private_variable)  # 출력: 5


# 상속
class GenderException(Exception):
    pass


class Animal:  # 부모 클래스
    def __init__(self, species, gender="Male"):
        self.species = species
        self.__gender = gender

    def make_sound(self):
        print("Some generic animal sound")

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender_type):
        if gender_type != "Male" or gender_type != "Female":
            raise GenderException("잘못된 성별, Male/Female 중 하나여야 함")
        self.__gender = gender_type


class Dog(Animal):  # 자식 클래스
    def __init__(self, name):
        super().__init__("Dog")  # 부모 클래스의 생성자 호출
        self.name = name

    def make_sound(self):  # 메서드 오버라이딩
        print("Woof!")


dog = Dog("Buddy")
print(dog.species)  # 출력: Dog
print(dog.name)  # 출력: Buddy
print(dog.gender)
dog.make_sound()  # 출력: Woof!


# Composition
class Engine:
    def start(self):
        print("Engine starting")


class Car:
    def __init__(self):
        self.engine = Engine()  # Engine 클래스의 인스턴스를 포함

    def start(self):
        self.engine.start()  # 포함된 Engine 인스턴스의 메서드 호출
        print("Car starting")


car = Car()
car.start()
# 출력:
# Engine starting
# Car starting
