def add_one(some_list: list[int]) -> list:
    """
    The function takes a list of digits, combines them into a single number,
    adds 1 to it, and converts the result back into a list of digits.
    parameter: list of digits
    return: updated list of digits
    """
    num = int("".join(map(str, some_list)))
    res = num + 1
    result = list(map(int, str(res)))
    return result


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")