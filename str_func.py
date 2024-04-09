def capitalize_all_letters(text):
    """
    Capitalize all letter in string.
    """
    return text.upper()

def capitalize_first_letters(text):
    """
    Capitalize first letters in all words
    """
    return " ".join(word.capitalize() for word in text.split())
