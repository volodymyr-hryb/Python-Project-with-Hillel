def is_even(number: int) -> bool:
    """ A function that checks if a number is even.
        parameter: number
        return: boolean
        """
    nums = ["0", "2", "4", "6", "8"]
    number_string = str(number).replace("-", "")
    last = number_string[-1]
    return last in nums


assert is_even(2494563894038**2) == True
assert is_even(1056897**2) == False
assert is_even(24945638940387**3) == False
print('Ok')