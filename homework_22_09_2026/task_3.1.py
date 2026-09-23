num_1 = float(input("Введіть перше число: "))
num_2 = float(input("Введіть друге число: "))
oper = input("Оберіть дію ('+' - додавання, '-' - віднімання, '*' - множення, '/' - ділення): ")
if oper == "+":
    res = num_1 + num_2
    print(round(res, 1))
elif oper == "-":
    res = num_1 - num_2
    print(round(res, 1))
elif oper == "*":
    res = num_1 * num_2
    print(round(res, 2))
elif oper == "/":
    if num_2 == 0:
        print("Помилка: ділення на нуль!")
    else:
        res = num_1 / num_2
        print(round(res, 2))
else:
    print("Помилка! У Вас є лише 4 варіанта.")