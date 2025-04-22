# Converter to convert a string to snake case from PascalCase and camelCase


# Using for loop
def convert_to_snake_case_1(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
            converted_character = '_' + char.lower()
            snake_cased_char_list.append(converted_character)
        else:
            snake_cased_char_list.append(char)
    snake_cased_string = ''.join(snake_cased_char_list)
    clean_snake_cased_string = snake_cased_string.strip('_')

    return clean_snake_cased_string

# Using list comprehension
def convert_to_snake_case_2(pascal_or_camel_cased_string):
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')


# Entry point of the program
def main():
    print(convert_to_snake_case_1('camelLongAndComplexString'))
    print(convert_to_snake_case_2('PascalLongAndComplexStringWithNumbers123'))


# Call the main function to run the program
main()
