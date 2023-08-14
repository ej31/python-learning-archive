# empty_tuple = ()
# tuple_type_1 = (100,)
# tuple_type_2 = (1, 2, 3, 4, "hello", "this is text")
#
# print(tuple_type_2[0])
# print(tuple_type_2[1])
# print(tuple_type_2[2])
# print(tuple_type_2[5])
#
# # 튜플의 길이 확인
# tuple_type_2 = (1, 2, 3, 4, "hello", "this is text")
# type_2_length = len(tuple_type_2)
# print(type_2_length)
# # 길이는 언제나 인덱스 + 1
# # off-by-one issue
#
# # 튜플 slice
# fruits_tuple = ('apple', 'banana', 'orange', 'grape', 'melon')
# # 0번부터 2번 인덱스까지 출력
# after_slice_type_1 = fruits_tuple[0:3]
# print(f"{after_slice_type_1} == {fruits_tuple[0:3]}")
#
# after_slice_type_2 = fruits_tuple[::-1]
# print(f"{after_slice_type_2} == {fruits_tuple[::-1]}")
#
# after_slice_type_3 = fruits_tuple[2:]
# print(f"{after_slice_type_3} == {fruits_tuple[2:]}")
#
# after_slice_type_4 = fruits_tuple[:4]
# print(f"{after_slice_type_4} == {fruits_tuple[:4]}")
#
# # 튜플과 zip() 함수
# fruits = ('apple', 'banana', 'orange')
# prices = (1.2, 0.9, 1.5)
# quantities = (3, 5, 2)
#
# ## 이어서...
# ## 이어서...
# ## 이어서...
#
# zip_fruits_info = zip(fruits, prices, quantities)
# print(zip_fruits_info)
#
# convert_with_iterator = list(zip_fruits_info)
# print(f"convert_with_iterator -- {convert_with_iterator}")
#
# # 튜플 언패킹
# for tuple_element in convert_with_iterator:
#     __fruit, __price, __quantity = tuple_element
#     print(f"tuple_element - - {tuple_element} // __fruit : {__fruit} , __price : {__price}, __quantity : {__quantity}")

# index(), count()
fruits = ('apple', 'banana', 'banana', 'banana', 'orange', 'cherry', 'melon')
# index() -- 안쪽에 선언 된 값이 몇번 인덱스에 있는지 찾는다. 없을 경우 에러
print(fruits.index('orange'))
# count() -- 안쪽에 선언 된 값이 몇번 등장하는지 알려준다. 없을 경우 0
print(fruits.count("orange"))
