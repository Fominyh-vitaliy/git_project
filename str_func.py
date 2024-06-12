def to_uppercase(string):
    """                                                                                                               Функция принимает строку и возвращает ее со всеми заглавными буквами.
    """
    return string.upper()


def capitalize_words(s):
    """
    Функция принимает строку и делает заглавными первые буквы каждого слова в этой строке
    """
    return ' '.join(word.capitalize() for word in s.split())
