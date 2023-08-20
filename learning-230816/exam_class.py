class Mouse:

    def __init__(self, color, button_cnt, name):
        self.__color = color
        self.__cnt = button_cnt
        self.__name = name

    def color(self):
        return f"색상은 {self.__color} 입니다."

    def btn_count(self):
        return f"마우스버튼은 {self.__cnt}개 입니다."

    def brand(self):
        return f"이 마우스의 브랜드는 {self.__name} 입니다."


royche_btn5_mouse = Mouse("Black", 5, "MUS-001")
print(f"마우스 color == {royche_btn5_mouse.color()} ")
print(f"마우스 btn_count == {royche_btn5_mouse.btn_count()} ")
print(f"마우스 brand == {royche_btn5_mouse.brand()} ")
print()
abnormal_btn10_mouse = Mouse(color="Red", button_cnt=100, name="ABNORMAL-MUS-001")
print(f"마우스 color == {abnormal_btn10_mouse.color()} ")
print(f"마우스 btn_count == {abnormal_btn10_mouse.btn_count()} ")
print(f"마우스 brand == {abnormal_btn10_mouse.brand()} ")
