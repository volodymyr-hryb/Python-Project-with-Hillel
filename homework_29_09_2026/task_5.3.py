import string

name = input("Введіть рядок: ").title()

translation_table = str.maketrans("", "", string.punctuation + " ")
new_name = name.translate(translation_table)

if len(new_name) != 0:
    hashtag = "#" + new_name
    print(hashtag[:140])
else:
    print("Рядок пустий!")



