def common_elements():
    evens_3 = (x for x in range(100) if x % 3 == 0)
    evens_5 = (x for x in range(100) if x % 5 == 0)
    evens_set_3 = set(evens_3)
    evens_set_5 = set(evens_5)
    result = evens_set_3 & evens_set_5
    print(result)
    return result


common_elements()