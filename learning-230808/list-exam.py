import copy

# this_is_list = ["hello", "world", "hi", "three", "four", "five"]
# print(this_is_list[0])
#
# this_is_list[0] = "hihihihihi"
# print(this_is_list[0])
#
# this_is_txt = "helloWorld!"
# for txt in this_is_txt:
#     print(txt)
#
# this_is_tuple = ("123", "12312313")
# print(this_is_tuple)
#
#
# this_is_list = ["a", "b", "c", "d", "e"]
# print(f"this_is_list (f 요소 추가 전) -- {this_is_list}")
# this_is_list.append("f")
# print(f"this_is_list (f 요소 추가 후) -- {this_is_list}")
#
# this_is_list.insert(1, "z")
# print(f"this_is_list (z 요소 1번에 추가 후) -- {this_is_list}")
#
# a = print
# a("asd")
#
# my_list = ["a", "b", "c", "d", "e", "f", "g"]
# print(f"del my_list 원본 \t\t\t {my_list}")
# del my_list[0]
# print(f"del my_list[0]을 날린 상태 \t {my_list}")
#
# try:
#     my_list.remove("ee")
#     print(my_list)
# except ValueError as e:
#     print("없는 값입니다!")
#
# my_list.remove("e")
# print(f"'e' 값을 날린 상태 \t\t\t {my_list}")
#
# this_is_mylist_first_element_by_pop = my_list.pop(0)
# print(f"0번 pop한 상태 \t\t\t\t {my_list}")
# print(f"0번 값 \t\t\t\t\t\t {this_is_mylist_first_element_by_pop}")
#
# ## 리스트 슬라이싱
# list_for_slice = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
#
# print(list_for_slice[1:9:2])  # 1번 인덱스부터 2개씩 건너뛰고 8번째 인덱스까지 감
# print(list_for_slice[1:5])  # 1번 인덱스부터 4번인덱스까지 자름
# print(list_for_slice[::-1])  # 역순으로 진행
# print(list_for_slice[::-2])  # 역순으로 두개씩 건너뛰어서 자름
#
#
#

# def some_function(some_list: []):
#     some_list[0] = "aa"
#
#
# some_list_1st = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
# some_function(some_list_1st)  # 0번 인덱스가 "aa"로 바뀌어있음
#
# print(some_list_1st)
# list_for_copy_issue_1st = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
# list_for_copy_issue_2nd = list_for_copy_issue_1st
#
# print(f"원본상태 - list_for_copy_issue_1st -- {list_for_copy_issue_1st}")
# print(f"원본상태 - list_for_copy_issue_2nd -- {list_for_copy_issue_2nd}")
#
# list_for_copy_issue_2nd[0] = "안녕하세요"
#
# print(f"2번 리스트 0번 인덱스만 바꾼 상태 - list_for_copy_issue_1st -- {list_for_copy_issue_1st}")
# print(f"2번 리스트 0번 인덱스만 바꾼 상태 - list_for_copy_issue_2nd -- {list_for_copy_issue_2nd}")
#

# deep copy case.1
copy_list_1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
copy_list_2 = copy_list_1.copy()
copy_list_2[0] = "반갑다리"
print(f"copy_list_1 -- {copy_list_1}")
print(f"copy_list_2 -- {copy_list_2}")

# deep copy case.2
copy_list_3 = copy.deepcopy(copy_list_1)
copy_list_3[0] = "반갑다리"
print(f"copy_list_1 -- {copy_list_1}")
print(f"copy_list_3 -- {copy_list_3}")
