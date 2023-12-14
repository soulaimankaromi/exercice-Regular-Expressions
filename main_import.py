from import_re import search_word_in_string,contains_digits,replace_spaces_with_dashes,valid_phone_number,is_valid_email
# Example usage:
word_result = search_word_in_string('eat', 'I eat a sandwitch.')
print(word_result)

digit_result = contains_digits('worldcup2022')
print(digit_result)

space_result = replace_spaces_with_dashes('i dont like bla bla bla')
print(space_result)

phone= valid_phone_number('06-166-1620')
print(phone)

email= is_valid_email('example@gmail.com')
print(email)