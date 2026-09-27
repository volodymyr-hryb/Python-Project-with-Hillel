import random

list_length = random.randint(3, 10)
main_list = []
for i in range(list_length):
    number = random.randint(1, 10)
    main_list.append(number)

new_list = [main_list[0], main_list[2], main_list[-2]]
print(main_list)
print(new_list)