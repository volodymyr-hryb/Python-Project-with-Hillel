def popular_words(text:str, words:list) -> dict:
    """
    The function counts the occurrences of each word from a given list in a string.
    parameter: string, list of words
    return: dictionary (word: count)
    """
    text_lower = text.lower()
    words_list = text_lower.split()

    result_dict = {}

    for word in words:
        count = words_list.count(word)
        result_dict[word] = count

    return result_dict


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 },'Test1'
print('OK')