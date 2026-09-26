l = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
if len(l) != 0:
    only_zero = []
    only_numbers = []
    for i in l:
        if i == 0:
            only_zero.append(0)
        else:
            only_numbers.append(i)
    new_list = only_numbers + only_zero
    print(new_list)
else:
    print("Список порожній!")