def to_uppercase(string):
    return string.upper()


def capitalize_words(s):
    """
    Функция принимает строку и делает заглавными первые буквы каждого слова в этой строке
    """
    return ' '.join(word.capitalize() for word in s.split())
