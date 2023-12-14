import re

# Exercice 1
def search_word_in_string(word, chain):
    return bool(re.search(fr'\b{re.escape(word)}\b', chain))

# Exercice 2
def contains_digits(s):
    return bool(re.search(r'\d', s))

# Exercice 3
def replace_spaces_with_dashes(text):
    return re.sub(r' ', '-', text)

# Exercice 4
def valid_phone_number(number):
    return bool(re.match(r'\d{2}-\d{3}-\d{4}', number))

# Exercice 5
def is_valid_email(email):
    return bool(re.match(r'\b[A-z0-9\.]+@[A-z0-9]+\.[A-z]{2,}\b', email))