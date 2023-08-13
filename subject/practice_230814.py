"""정수 리스트를 입력받아, 그 중 짝수만을 반환하는 함수 even_numbers를 작성해보세요."""


# 'even_numbers' 함수를 정의합니다. 이 함수는 정수 리스트를 입력받아 짝수만을 반환합니다.
def even_numbers(numbers):
    # 짝수를 저장할 빈 리스트를 생성합니다.
    even_list = []

    # 입력받은 숫자 리스트를 반복하면서 각 숫자를 확인합니다.
    for number in numbers:
        # 숫자가 짝수인 경우
        if number % 2 == 0:
            # 짝수 리스트에 추가합니다.
            even_list.append(number)

    # 짝수만 포함된 리스트를 반환합니다.
    return even_list


# 예제로 사용할 숫자 리스트
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 'even_numbers' 함수를 호출하고 결과를 출력합니다.
print(even_numbers(numbers))  # 출력: [2, 4, 6, 8]

"""문자열을 입력받아, 그 문자열을 거꾸로 뒤집은 결과를 반환하는 함수 reverse_string를 작성해보세요."""


# 'reverse_string' 함수를 정의합니다. 이 함수는 문자열을 입력받아 거꾸로 뒤집은 결과를 반환합니다.
def reverse_string(s):
    # 문자열을 거꾸로 뒤집어 반환합니다.
    return s[::-1]


# 예제로 사용할 문자열
example_string = "파이썬"

# 'reverse_string' 함수를 호출하고 결과를 출력합니다.
print(reverse_string(example_string))  # 출력: "썬이파"

"""리스트의 모든 요소를 더하는 함수 sum_elements를 작성해보세요."""


# 'sum_elements' 함수를 정의합니다. 이 함수는 리스트의 모든 요소를 더해 반환합니다.
def sum_elements(elements):
    # 합계를 저장할 변수를 0으로 초기화합니다.
    total = 0

    # 리스트의 모든 요소를 반복하면서 더합니다.
    for element in elements:
        total += element

    # 최종 합계를 반환합니다.
    return total


# 예제로 사용할 리스트
numbers = [10, 20, 30, 40, 50]

# 'sum_elements' 함수를 호출하고 결과를 출력합니다.
print(sum_elements(numbers))  # 출력: 150

"""정수 리스트를 입력받아, 그 중 가장 큰 수와 가장 작은 수를 반환하는 함수 find_max_min를 작성해보세요."""


# 'find_max_min' 함수를 정의합니다. 이 함수는 정수 리스트를 입력받아 가장 큰 수와 가장 작은 수를 반환합니다.
def find_max_min(numbers):
    # 리스트의 첫 번째 요소로 최대값과 최소값을 초기화합니다.
    max_number = numbers[0]
    min_number = numbers[0]

    # 위의 코드는 아래와 같이 줄여서 표현 할 수 있습니다.
    # max_number = min_number = numbers[0]

    # 리스트의 모든 요소를 반복하면서 최대값과 최소값을 찾습니다.
    for number in numbers:
        if number > max_number:
            max_number = number
        if number < min_number:
            min_number = number

    # 최대값과 최소값을 반환합니다.
    return max_number, min_number


# 예제로 사용할 정수 리스트
numbers = [34, 12, 56, 78, 23]

# 'find_max_min' 함수를 호출하고 결과를 출력합니다.
print(find_max_min(numbers))  # 출력: (78, 12)

"""문자열을 입력받아, 그 문자열에 포함된 모든 모음의 개수를 반환하는 함수 count_vowels를 작성해보세요."""


# 'count_vowels' 함수를 정의합니다. 이 함수는 문자열을 입력받아 모든 모음의 개수를 반환합니다.
def count_vowels(s):
    # 모음을 정의합니다.
    vowels = 'aeiouAEIOU'

    # 모음의 개수를 저장할 변수를 0으로 초기화합니다.
    count = 0

    # 문자열의 모든 문자를 반복하면서 모음의 개수를 세어줍니다.
    for char in s:
        if char in vowels:
            count += 1

    # 모음의 개수를 반환합니다.
    return count


# 예제로 사용할 문자열
string = "Hello, Python!"

# 'count_vowels' 함수를 호출하고 결과를 출력합니다.
print(count_vowels(string))  # 출력: 4

"""문자열을 입력받아, 그 문자열에서 각 알파벳 문자가 몇 번 등장하는지를 사전 형태로 반환하는 함수 alphabet_frequency를 작성해보세요."""


# 'alphabet_frequency' 함수를 정의합니다. 이 함수는 문자열을 입력받아 각 알파벳 문자의 빈도를 사전 형태로 반환합니다.
def alphabet_frequency(s):
    # 알파벳 빈도를 저장할 빈 딕셔너리를 생성합니다.
    frequency_dict = dict()

    # 문자열의 모든 문자를 반복하면서 알파벳 문자의 빈도를 계산합니다.
    for char in s:
        if char.isalpha():  # 문자가 알파벳인 경우만 처리합니다.
            frequency_dict[char] = frequency_dict.get(char, 0) + 1

    # 알파벳 빈도 사전을 반환합니다.
    return frequency_dict


# 예제로 사용할 문자열
string = "Hello, Python!"

# 'alphabet_frequency' 함수를 호출하고 결과를 출력합니다.
print(alphabet_frequency(string))  # 출력: {'H': 1, 'e': 1, 'l': 2, 'o': 2, 'P': 1, 'y': 1, 't': 1, 'h': 1, 'n': 1}
