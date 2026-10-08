num = input("Введіть число від 0 до 8640000: ")
if len(num) == 0:
    print("Ви не ввели число!")
elif num.startswith('-') and num[1:].isdigit():
    print("Ви ввели від'ємне число!")
elif not num.isdigit():
    print("Ви ввели некоректні символи (букви або спецсимволи)!")
else:
    num = int(num)
    num_days = num // 86400
    num_hours = (num % 86400) // 3600
    num_mins = ((num % 86400) % 3600) // 60
    num_secs = ((num % 86400) % 3600) % 60
    last = str(num_days)[-1]
    if len(str(num_days)) == 1:
        if last in ["0", "5", "6", "7", "8", "9"]:
            days = "днів"
        elif last == "1":
            days = "день"
        else:
            days = "дні"
    else:
        two_last = str(num_days)[-2:]
        if two_last in ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"] or last in ["0", "5", "6", "7", "8", "9"]:
            days = "днів"
        elif two_last[-1] == "1":
            days = "день"
        else:
            days = "дні"
    hours_str = str(num_hours).zfill(2)
    mins_str = str(num_mins).zfill(2)
    secs_str = str(num_secs).zfill(2)

    print(f"{num_days} {days}, {hours_str}:{mins_str}:{secs_str}")