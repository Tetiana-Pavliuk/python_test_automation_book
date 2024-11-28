import re


def contains_characters(string, chars):
    pattern = ''.join(f'(?=.*{re.escape(char)})' for char in chars)
    print(bool(re.search(pattern, string)))

contains_characters('7865serS3', '973')

def count_uppercase(input_string):
    uppercase_letters = re.findall(r'[A-Z]', input_string)
    print(f'Number of capital letters: {len(uppercase_letters)}')

count_uppercase('7865serS3')

def contains_upper_case_followed_by_lower_case(input_string):
    pattern = r'[A-Z][a-z]+'
    match = re.search(pattern, input_string)
    if match:
        print('True')
    else:
        print('False')

contains_upper_case_followed_by_lower_case('7865serS3')