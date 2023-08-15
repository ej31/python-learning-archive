# 클래스 정의 (자동차 틀)
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self.is_running = False

    def start_engine(self):
        if not self.is_running:
            print(f"{self.color} 색상 {self.model} 모델 자동차의 엔진이 시작되었습니다.")
            self.is_running = True
        else:
            print("이미 엔진이 작동 중입니다.")

    def accelerate(self):
        if self.is_running:
            print(f"{self.color} 색상 {self.model} 모델 자동차가 가속 중입니다.")
        else:
            print("먼저 엔진을 시작하세요.")

    def stop(self):
        if self.is_running:
            print(f"{self.color} 색상 {self.model} 모델 자동차가 정지되었습니다.")
            self.is_running = False
        else:
            print("이미 엔진이 꺼져 있습니다.")


# 객체 생성 (실제 자동차)
red_car = Car(color="빨간", model="세단")
blue_car = Car(color="파란", model="SUV")

# 객체의 메서드 호출 (자동차 작업)
red_car.start_engine()
red_car.accelerate()
red_car.stop()

blue_car.start_engine()
blue_car.accelerate()




