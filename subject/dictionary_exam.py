def dictionary_case_1():
    """
    1. 기존 값 업데이트 및 새로운 값 추가:
    """
    # 원본 Dictionary 생성
    original_dict = {'apple': 2, 'banana': 3, 'cherry': 5}
    print("원본 Dictionary:", original_dict)

    # 업데이트할 Dictionary 생성
    update_dict = {'banana': 4, 'orange': 6}

    # update() 메서드를 사용하여 원본 Dictionary 업데이트
    original_dict.update(update_dict)

    # 출력 결과와 설명
    print("업데이트된 Dictionary:", original_dict)
    # 업데이트된 Dictionary: {'apple': 2, 'banana': 4, 'cherry': 5, 'orange': 6}


def dictionary_case_2():
    """
    2. 빈 Dictionary로 업데이트하기
    """

    # 원본 Dictionary 생성
    person_info = {'name': 'John', 'age': 30}

    # 빈 Dictionary로 업데이트
    empty_dict = {}

    person_info.update(empty_dict)

    # 출력 결과와 설명
    print("업데이트된 정보:", person_info)
    # 업데이트된 정보: {'name': 'John', 'age': 30}


def dictionary_case_3():
    """
    3. 업데이트할 Dictionary가 비어있는 경우
    """

    # 원본 Dictionary 생성
    fruit_counts = {'apple': 10, 'banana': 15}

    # 업데이트할 Dictionary 생성
    empty_dict = {}

    # update() 메서드 사용
    fruit_counts.update(empty_dict)

    # 출력 결과와 설명
    print("업데이트된 과일 개수:", fruit_counts)
    # 업데이트된 과일 개수: {'apple': 10, 'banana': 15}


if __name__ == '__main__':
    print(__name__)
    dictionary_case_1()
    dictionary_case_2()
    dictionary_case_3()
