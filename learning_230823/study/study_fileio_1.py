import logging
import traceback
class InvalidArgumentException(Exception):
    pass


def add(v1, v2):
    print(f"add -- (1) v1: {v1}, v2: {v2}")
    if v1 is None or v2 is None:
        raise InvalidArgumentException("일부러 터트렸습니다!")
    print(f"add -- (2) v1: {v1}, v2: {v2}")


def div(v1, v2):
    print(f"add -- (1) v1: {v1}, v2: {v2}")
    if v1 is None or v2 is None:
        raise ZeroDivisionError("0으로 나눌수 없습니다!")
    print(f"add -- (2) v1: {v1}, v2: {v2}")


if __name__ == '__main__':
    try:
        print("Hello Python World!")
        add(1, 2)
        add(1, None)
        print("try 끝점까지 도달했습니다.")
        logging.basicConfig()
    except (InvalidArgumentException, ZeroDivisionError) as e:
        print(e)
        print("예외처리를 시작합니다")
    else:
        print("ELSE")
    finally:
        print("!")

    print("프로그램을 종료합니다.")
