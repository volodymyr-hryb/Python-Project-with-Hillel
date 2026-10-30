def generate_cube_numbers(end: int):
    """ A function that generates a set of cubes of numbers, starting from 2 up to the specified value.
        parameter: number
        return: list of numbers
        """
    for num in range(2, end):
        number = num ** 3
        if number > end:
            return
        else:
            yield number


from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True
assert list(generate_cube_numbers(10)) == [8]
assert list(generate_cube_numbers(100)) == [8, 27, 64]
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000]
print('Ok')


