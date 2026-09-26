l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if len(l) != 0:
    last_element = l[-1]
    i = 0
    summ = 0
    while i < len(l):
        if i % 2 == 0:
            summ += l[i]
        i += 1
    print(summ * last_element)
else:
    print(0)


# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_l = sum(l[::2]) * l[-1]
# print(new_l)