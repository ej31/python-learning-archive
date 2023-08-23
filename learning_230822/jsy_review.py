from typing import Optional


class SebinClass:
    this_is_cls_var = "Hello junseon world!"

    def __init__(self):
        self.__instance_variable = "Hello World!"
        self.__second_variable: Optional[str] = None
        print("Hello Sebin world!")

    @classmethod
    def get_class_variable(cls):
        return cls.this_is_cls_var

    def get_instance_variable(self):
        return self.__instance_variable


def app():
    _sebin = SebinClass
    _sebin.get_class_variable()
    _sebin.get_instance_variable()


if __name__ == '__main__':
    _v = "Hello"
    _w = "World"
    print(_v, " ", _w)
    print(f"  {{feofooejofefjefo}}  {_v} {_w}")
