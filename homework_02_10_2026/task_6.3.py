num = abs(int(input("Введите целое число: ")))

while True:
    if num <= 9:
        break
    product = 1
    for el in str(num):
        product *= int(el)
    num = product

print(num)
