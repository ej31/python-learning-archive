empty_set = {}

set_type_1 = {10, 20}
set_type_2 = {"hello", "Python!"}

# set_type_1_1 = set([10, 20])
# set_type_1_2 = set(["hello", "Python!"])

# set 요소 추가 및 갱신
set_fruit = {"apple", "banana", "mango", "cherry"}
print(f"set_fruit before add -- {set_fruit}")
set_fruit.add("melon")
print(f"set_fruit after add -- {set_fruit}")

set_fruit.update(("strawberry", "blueberry"))
print(f"set_fruit after update -- {set_fruit}")

# set 요소 삭제
set_fruit_type_2 = {"apple", "banana", "mango"}
set_fruit_type_2.remove("appleeeeee")
print(f"set_fruit_type_2 after remove -- {set_fruit_type_2}")

set_fruit_type_2.discard("apple")
print(f"set_fruit_type_2 after remove -- {set_fruit_type_2}")


