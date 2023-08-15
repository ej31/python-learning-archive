# apple_box라는 변수에 10을 할당
apple_box = 10

# 함수 밖에서 이름이 정해지고 값의 대입이 이루어지는 변수를 전역변수라 한다.
# 코드 파일 내 클래스나 메서드에서도 접근이 가능하다.
global_variable = 10


def some_function():
    # 함수 안의 변수를 지역변수라고 한다.
    local_variable = 999
    print(f"(1) global_variable 변수는, {global_variable}")
    print(f"(2) local_variable 변수는, {local_variable}")


some_function()  # 출력 결과: 10

print(f"(3) global_variable 변수는, {global_variable}")


# print(f"(4) local_variable 변수는, {local_variable}") # "NameError" 발생.


def function_a():
    a = 100
    ...


def function_b():
    b = 100
    ...


def outer_function():
    outer_variable = 30  # outer_function() 내의 지역 변수

    def inner_function():
        inner_variable = 40  # inner_function() 내의 지역 변수
        print(inner_variable)  # 출력 결과: 40

    inner_function()
    print(outer_variable)  # 출력 결과: 30


outer_function()

# 아래 줄은 오류를 발생시킵니다. inner_function() 내의 지역 변수인 inner_variable에 접근하려 했지만 해당 변수는 inner_function() 내부에서만 유효합니다.
# print(inner_variable)


# 변수 이름 겹치는 경우
global_variable = 10  # 전역 범위에 있는 변수


def function_with_same_name():
    global_variable = 20  # function_with_same_name() 내의 지역 변수
    print(global_variable)  # 출력 결과: 20


function_with_same_name()  # function_with_same_name() 호출
print(global_variable)  # 출력 결과: 10


def example_function():
    local_variable = 10
    print(local_variable)


example_function()  # 함수 호출, 출력 결과: 10


# 함수가 종료되었으므로 local_variable은 더 이상 유효하지 않습니다.
# 아래 줄은 오류를 발생시킵니다.
# print(local_variable)


