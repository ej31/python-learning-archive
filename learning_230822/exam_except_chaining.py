def divide_numbers(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        raise ValueError("y cannot be zero") from e
    return result


try:
    print(divide_numbers(10, 0))
except ValueError as e:
    print(e)
    print(e.__cause__)
