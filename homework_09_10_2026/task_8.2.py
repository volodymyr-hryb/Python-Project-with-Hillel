def is_palindrome(string_in: str) -> bool:
    """
    A function that takes a string and checks if it is a palindrome.
    parameter: string
    return: True if string is a palindrome, False otherwise
    """
    import string
    spec_chars = string.punctuation
    translation_table = str.maketrans("", "", spec_chars)
    text = string_in.lower().strip().replace(' ', '').translate(translation_table)
    reversed_text = text[::-1]
    return reversed_text == text


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")