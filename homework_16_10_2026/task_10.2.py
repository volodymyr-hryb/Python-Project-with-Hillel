def first_word(text:str) -> str:
    """
    A function that accepts a string and finds the first word in it.
    parameter: string
    return: first word of string
    """
    import re
    text_without_symbols_at_sides = re.sub(r"^[^a-zA-Zа-яА-ЯёЁ]+|[^a-zA-Zа-яА-ЯёЁ]+$", "", text)
    text_without_symbols_inside = re.sub(r"[^\w\s']", " ", text_without_symbols_at_sides)
    words_list = text_without_symbols_inside.split()

    return words_list[0]


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
