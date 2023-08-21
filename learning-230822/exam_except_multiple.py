
try:
    # 예외를 발생시킬 수 있는 일부 코드
    pass
except (TypeError, ValueError) as e:
    print(f"Caught an exception: {e}")
