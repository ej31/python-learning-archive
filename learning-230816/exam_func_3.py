from dataclasses import dataclass


def default_parameter_exam(param1, param2, param3=100):
    if param3 is None:
        param3 = [1, 2, 3]
    print(param1)
    print(param2)
    print(param3)
    pass


# default_parameter_exam(10, param1=10, param2=20, param3=30)


def dynamic_parameter(*args):
    for arg in args:
        print(arg)
    print([arg for arg in args])


def dynamic_keyword_argument_case_1(**kwargs):
    # print([item for item in kwargs.items()])
    for item in kwargs.items():
        print(item)


def dynamic_keyword_argument_case_2(*args, **kwargs):
    # print([item for item in kwargs.items()])
    for item in kwargs.items():
        print(item)

    for item in kwargs.items():
        print(item)


dynamic_parameter([1, 2, 3, 4, 5], 11, 22, 33, 44, 55, 55, 66, 77, 88)
dynamic_keyword_argument_case_1(수강생1="홍길동", 수강생2="김갑수")

dynamic_keyword_argument_case_2(1, 2, 3, 4, 5, 수강생1="홍길동", 수강생2="김갑수")


# def dynamic_keyword_argument_case_3(**args1, **args2):
#     pass
#
#
# dynamic_keyword_argument_case_3(수강생1="홍길동", 수강생2="김갑수", 수강생1="홍길동", 수강생2="김갑수")

# def invalid_args_position(*args, **kwargs):
#     if "param1" not in kwargs:
#         raise Exception()
#
#
# invalid_args_position(1, 2, 3, 4, 5, param1="ABC")

@dataclass
class UserInfoDto:
    name: str
    age: int
    height: int
    weight: int


def get_user_info(user_id):
    """
    유저 정보를 가져올 수 있습니다.
    :param user_id:
    :return: 첫번째 값은 이름, 두번째 값은 나이, 세번째는 키, 네번째는 몸무게입니다. 실수하지마세요!
    """
    if 1 == user_id:  # 원래는 데이터베이스에서 가져와야 하는 부분
        return UserInfoDto("홍길동", 30, 184, 85)  # DTO Class


def get_user_name(user_id):
    if 1 == user_id:  # 원래는 데이터베이스에서 가져와야 하는 부분
        return "홍길동"


def get_user_age(user_id):
    if 1 == user_id:  # 원래는 데이터베이스에서 가져와야 하는 부분
        return "홍길동"


def get_user_height(user_id):
    if 1 == user_id:  # 원래는 데이터베이스에서 가져와야 하는 부분
        return "홍길동"


def get_user_weight(user_id):
    if 1 == user_id:  # 원래는 데이터베이스에서 가져와야 하는 부분
        return "홍길동"


# user_info = get_user_info(1)
# print(user_info)


def return_none_function_case1():
    return


def return_none_function_case2():
    print("아무것도 리턴하지 않아요")


def return_none_function_case3(param1=None):
    if param1 is None:
        # do something..
        pass


def validation_row():
    # TODO: 행 검사해야함
    pass


def get_row_in_csv():
    # TODO : CSV 가져오는 행동
    pass


print(f"case 1 -- {return_none_function_case1()}")
print(f"case 2 -- {return_none_function_case2()}")
