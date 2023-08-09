# from dataclasses import dataclass
#
# empty_list_type1 = [1, 2, 3, 4, "aasa"]
# empty_list_type2 = list([1, 2, 3, 4])
#
#
# @dataclass
# class SomeType:
#     some_int: int
#     some_str: str
#
#
# empty_list_type3 = [SomeType(1, "123")]
#
# empty_list_type1.append("apple")
# empty_list_type1.append("pineapple")
# empty_list_type1.append("grape")
#
# print(empty_list_type1)
#
# ## 리스트 인덱싱 슬라이싱
# list_indexing_sample = ["apple", "grape", "mango"]
#
# print(list_indexing_sample[2])
#
# # 슬라이싱
# list_indexing_sample.append("watermelon")
# list_indexing_sample.append("orange")
# list_indexing_sample.append("lemon")
# list_indexing_sample.append("banana")
#
# print(list_indexing_sample[0:2])
#
# "[2023-08-08] somedata...."
# "[2023-08-08] somedata....2"
# "[2023-08-08] somedata....3"
# "[2023-08-08] somedata....4"
# "[2023-08-08] somedata....5"
# "[2023-08-09] somedata....6"
# "[2023-08-09] somedata....6"
# "[2023-08-09] somedata....6"
# "[2023-08-09] somedata....6"
# "[2023-08-09] somedata....6"
#
# print(int("[2023-08-08] somedata....3"[0:12].replace("[", "").replace("]", "").replace("-", "")))
#
# list_for_loop = list(["apple", "banana", "mango", "pineapple"])
#
# for fruit in list_for_loop:
#     print(fruit)
#
#     if fruit == "banana":
#         print("바나나 발견! 루프를 종료합니다.")
#
# list_for_comprehension = list(["apple", "banana", "mango", "pineapple"])
#
# list_post_process_fruit_list = [fruit + "____" for fruit in list_for_comprehension if fruit == "banana"]
#
# print(list_post_process_fruit_list)
#
# # 리스트 메서드 활용
# list_for_sort = ["mango", "banana", "apple", "pineapple"]
# list_for_sort_by_deepcopy = list_for_sort.copy()
# list_for_sort_by_deepcopy.sort()
#
# print(list_for_sort)
# print(list_for_sort_by_deepcopy)
#
# # 뒤집기
#
# list_for_reverse = ["mango", "banana", "apple", "pineapple"]
# list_for_reverse_by_deepcopy = list_for_reverse.copy()
# list_for_reverse_by_deepcopy.reverse()
#
# print(list_for_reverse)
# print(list_for_reverse_by_deepcopy)
#
# # 값 제거하기
# list_for_remove = ["apple", "mango"]
# list_for_remove.remove("apple")
# print(list_for_remove)
#
# # 길이 구하기
# list_for_length = ["mango", "banana", "apple", "pineapple"]
# print(list_for_length.__len__())
# print(len(list_for_length))


# # 다차원 리스트
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# for _array in matrix:
#     for _el in _array:
#         print(_el)
#
# # 리스트 병합 및 최대 최소값 찾기
#
# list_1 = ["mango", "banana", "apple", "pineapple"]
# list_2 = ["sweetpotato"]
#
# list_3 = list_1 + list_2
# print(list_3)
#
# list_for_minmax = [1, 2, 3, 4, 5]
#
# min_by_list_for_minmax = min(list_for_minmax)
# max_by_list_for_minmax = max(list_for_minmax)
#
# print(min_by_list_for_minmax)
# print(max_by_list_for_minmax)
#
# # 함수 평탄화
# list_for_flatten = [
#     [1, 32, ],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
#
# def list_flatter(matrix_list):
#     # 같은 로직이다.
#     ret = [__array_2 for __array in matrix_list for __array_2 in __array]
#     ret = []
#     for __array in matrix_list:
#         for __array_2 in __array:
#             ret.append(__array_2)
#
#     return ret
#
#
# print(list_flatter(list_for_flatten))
#
# fruits = ['apple', 'apple', 'banana', 'orange', 'banana', 'kiwi']
#
# apple_cnt = fruits.count("apple")
# print(apple_cnt)
#
# apple_cnt_type2 = 0
# for fruit in fruits:
#     if fruit == "apple":
#         apple_cnt_type2 += 1
#
# print(apple_cnt_type2)
#
# # 리스트 뒤집기
# fruits_type1 = ['apple', 'apple', 'banana', 'orange', 'banana', 'kiwi']
#
# # 슬라이싱 방식으로 뒤집기
#
# reverse_by_slice = fruits_type1[::-1]
# print(f"reverse_by_slice -- {reverse_by_slice}")
#
# # 리스트 내장 함수 사용해서 뒤집기
# fruits_type2 = ['apple', 'apple', 'banana', 'orange', 'banana', 'kiwi']
# fruits_type2.reverse()
# print(f"fruits_type2 -- {fruits_type2}")
#
# # 파이썬 내장함수를 이용해 뒤집기
# fruits_type3 = ['apple', 'apple', 'banana', 'orange', 'banana', 'kiwi']
# fruit_reverse_by_type3 = reversed(fruits_type3)
# print(fruit_reverse_by_type3)
# for fruit in fruit_reverse_by_type3:
#     print(fruit)

# fruits = ['apple', 'apple', 'banana', 'orange', 'banana', 'kiwi']
# idx_banana = fruits.index("apple")
# print(idx_banana)
#
# target_idx = []
# for i, fruit in enumerate(fruits):
#     print(i, fruit)
#     if fruit == "apple":
#         target_idx.append(i)
#
# print(target_idx)
#
# number_list = [10, 11, 21, 49, 15, 59, 62, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# even_numbers = [number for number in number_list if number % 2 == 0]
# print(even_numbers)
#
# larger_than_f = [number for number in number_list if number >= 50]
# print(larger_than_f)

# from typing import Iterable, Iterator
#
# fruits = ['apple', 'apple', 'banana', 'orange', 'banana', 'kiwi']
# iterator_fruits = iter(fruits)
# print(f"Iterator가...맞아?... {isinstance(iterator_fruits, Iterator)}")
#
# print(next(iterator_fruits))
# print(next(iterator_fruits))
# print(next(iterator_fruits))
# print(next(iterator_fruits))


# fruit_ids = [1, 2, 3]
# fruit_nms = ['apple', 'apple(상함)']
# fruit_price = [1000, 2000, 3000, 4000, 5000, 6000]
#
# zipped_fruits = zip(fruit_ids, fruit_nms, fruit_price)
# convert_to_list_fruit = list(zipped_fruits)
# print(convert_to_list_fruit)
#
# for _id, name, price in convert_to_list_fruit:
#     print(_id, name, price)

list_for_sort_type1 = ["mango", "banana", "apple", "pineapple"]
list_for_sort_type1.sort()
print(f"list_for_sort_type1 -- \t\t\t\t {list_for_sort_type1}")

list_for_sort_type1_rev = ["mango", "banana", "apple", "pineapple"]
list_for_sort_type1_rev.sort(reverse=True)
print(f"list_for_sort_type1_rev -- \t\t\t {list_for_sort_type1_rev}")

list_for_sort_type2 = ["mango", "banana", "apple", "pineapple"]
print(f"sorted(list_for_sort_type2) -- \t\t {sorted(list_for_sort_type2)}")
print(1 + 2)
