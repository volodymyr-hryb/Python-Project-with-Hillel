import keyword
import string

name = input("Введіть Ваш варіант назви змінної: ")
variant = True

if not name or name[0].isdigit():
    variant = False

for letter in name:
    if letter.isupper():
        variant = False

if name in keyword.kwlist:
    variant = False

if "__" in name:
    variant = False

bad_symbols = string.punctuation.replace("_", "") + " "

for char in name:
    if char in bad_symbols:
        variant = False

print(variant)