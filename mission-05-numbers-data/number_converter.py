"""
number_converter.py
-------------------
Asks for a decimal integer and displays its binary and hexadecimal equivalents.
"""

try:
    decimal_input = input("Enter a decimal integer: ")
    number = int(decimal_input)
    if number < 0:
        print("Please enter a positive integer.")
    else:
        binary_result = bin(number)      # e.g. 0b1101
        hex_result = hex(number)         # e.g. 0xd

        print(f"Decimal     : {number}")
        print(f"Binary      : {binary_result}  ({binary_result[2:]})")
        print(f"Hexadecimal : {hex_result}  ({hex_result[2:].upper()})")
except ValueError:
    print("Invalid input. Please enter a whole number.")
