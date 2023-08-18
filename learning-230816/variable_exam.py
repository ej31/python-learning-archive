this_is_variable = 10

sum_a = 100 + 10


def add(v1, v2):
    return v1 + v2


_ret_by_add_fn = add(10, 20)

global_var = 10000


def some_function():
    print(global_var)
    some_function_var = 100
    print("some_function")

    def some_function_2():
        print(global_var)
        some_2_var = 200

    some_function_2()
    # print(some_2_var)


some_function()

a = "Hey!"


def fn_1():
    a = 100
    print(a)


def fn_2():
    a = "Hello Python!"
    print(a)


fn_1()
fn_2()
