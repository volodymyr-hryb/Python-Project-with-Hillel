import string

user_input = input()

start_char, end_char = user_input.split("-")

letters = string.ascii_letters

start_pos = letters.index(start_char)
end_pos = letters.index(end_char)

print(letters[start_pos : end_pos + 1])
