_read = open("./myfile.txt", "r")
print(_read.read())
_read.close()

with open("myfile.txt", "r") as f:
    f.read()


class SomeClsss:
    def __init__(self):
        self.__some_obj = "Hello Object!"

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("끝! __exit__ 호출!")

    @staticmethod
    def do_something(self):
        print("do_something 메서드를 호출했습니다")


with SomeClsss() as some:
    print("시작")
