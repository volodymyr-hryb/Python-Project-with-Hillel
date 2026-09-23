lst = [1, 2, 3]
new_lst = []
if len(lst) % 2 == 0:
    mid = int(len(lst) / 2)
else:
    mid = int((len(lst) // 2) + 1)
first_part = lst[:mid]
second_part = lst[mid:]
new_lst.append(first_part)
new_lst.append(second_part)
print(new_lst)


