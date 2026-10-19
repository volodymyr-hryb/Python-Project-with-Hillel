def difference (*args: int|float) -> int|float:
    """
    The function finds the difference between the maximum and minimum values from a given set of numbers.
    parameter: any number of numbers
    return: difference between maximum and minimum number
    """
    if not args:
        return 0

    list_of_nums = list(args)
    minimum = min(list_of_nums)
    maximum = max(list_of_nums)
    diff = maximum - minimum

    return round(diff, 2)


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
