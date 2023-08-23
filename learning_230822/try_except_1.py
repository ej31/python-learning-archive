from exception_classes import InvalidNumberException


def div_number(v1, v2):
    if v2 == 0:
        raise InvalidNumberException("0을 집어넣으면 안됩니다!")
    return v1 / v2


class SomeClass:

    def __init__(self):
        pass

    @staticmethod
    def do_something():
        try:
            div_number(10, 0)
        except InvalidNumberException as e:
            print(e)
            print("에러를 잡았습니다!")
        else:
            pass
        finally:
            pass
        print("이 13번 라인 코드가 실행이 됐으면 좋겠다..")


if __name__ == '__main__':
    SomeClass().do_something()
