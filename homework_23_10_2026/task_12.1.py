def prime_generator(end: int):
    """ A function that generates a set of prime numbers, starting from 2 up to the specified value.
        parameter: number
        return: list of numbers
        """
    for num in range(2, end + 1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num


from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True
assert list(prime_generator(10)) == [2, 3, 5, 7]
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13]
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print('Ok')