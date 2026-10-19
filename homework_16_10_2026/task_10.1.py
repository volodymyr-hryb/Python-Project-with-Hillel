def pow(x):
    return x ** 2

def some_gen(begin: int, end: int, func):
    """
    Number sequence generator. Each subsequent number is created by applying 'func' to the previous number.
    begin: the first element of the sequence
    end: the number of elements in the sequence
    func: a function that generates sequence values
    """
    current = begin
    for _ in range(end):
        yield current
        current = func(current)

from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')