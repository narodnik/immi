#!/usr/bin/python
import csv
import sys
import random

# Src: https://github.com/arthurdejong/python-stdnum/blob/master/stdnum/luhn.py
def checksum(number, alphabet='0123456789'):
    """
    Calculate the Luhn checksum over the provided number.

    The checksum is returned as an int.
    Valid numbers should have a checksum of 0.
    """
    n = len(alphabet)
    number = tuple(alphabet.index(i)
                   for i in reversed(str(number)))
    return (sum(number[::2]) +
            sum(sum(divmod(i * 2, n))
                for i in number[1::2])) % n


def calc_check_digit(number, alphabet='0123456789'):
    """Calculate the extra digit."""
    check_digit = checksum(number + alphabet[0])
    return alphabet[-check_digit]

def main():
    with open("tac_codes.csv", "r") as csvf:
        # IMEI, BRAND, MODELS
        codes = list(csv.reader(csvf))

    tac_code, brand, model = random.choice(codes)

    # IMEIs will be generated based on the first 8 digits (TAC; the number
    #   used to identify the model) and the next 2-6 digits (partial serial #).
    #   The final, 15th digit, is the Luhn algorithm check digit.

    imei = tac_code

    # Randomly compute the remaining serial number digits
    while len(imei) < 14:
        imei += str(random.randint(0, 9))

    # Calculate the check digit with the Luhn algorithm
    imei += calc_check_digit(imei)

    print(f"IMEI: {imei} ({brand}, {model})")

if __name__ == '__main__':
    main()

