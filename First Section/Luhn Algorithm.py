# Luhn Algorithm
# The Luhn algorithm is a simple checksum formula used to validate a variety of identification numbers, such as credit card numbers.
# First, the number is reversed.
# Then, starting from the rightmost digit, the digits in odd positions are summed.
# The digits in even positions are doubled. If the result is greater than 9, the digits of the result are summed (e.g., 12 becomes 3).
# Finally, the total sum is calculated. If the total modulo 10 is equal to 0, the number is valid.


def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()