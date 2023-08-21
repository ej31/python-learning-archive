# try 블록 안에는 오류가 발생할 가능성이 있는 코드를 작성합니다.
try:
    # 숫자를 0으로 나누려고 시도합니다. 이는 ZeroDivisionError를 발생시킵니다.
    result = 10 / 0
except ZeroDivisionError:  # 특정 오류를 잡기 위한 except 블록
    # ZeroDivisionError가 발생하면 이 블록이 실행됩니다.
    print("0으로 나눌 수 없습니다.")
except Exception as e:  # 모든 오류를 잡기 위한 except 블록
    # 그 외의 오류가 발생하면 이 블록이 실행됩니다.
    print(f"오류 발생: {e}")
else:
    # 오류가 발생하지 않았을 때 실행됩니다.
    print(f"결과는 {result}입니다.")
finally:
    # 오류 발생 여부와 관계없이 항상 실행됩니다.
    print("예외 처리가 완료되었습니다.")


# 사용자 정의 예외 클래스
class MyException(Exception):
    pass


try:
    raise MyException("This is a custom exception")
except MyException as e:
    print(f"Caught an exception: {e}")
