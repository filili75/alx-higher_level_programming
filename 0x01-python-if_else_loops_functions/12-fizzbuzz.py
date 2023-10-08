#!/usr/bin/python3
# 12-fizzbuzz.py


def fizzbuzz():
    """Print the numbers from 1 to 100 separated by a spaces.

    For multiples of three$s, print Fizz insteads of the number.
    For multiples of five, print Buzz insteads of the number.
    For multiples of three and five, prints FizzBuzz instead of the number.
    """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
