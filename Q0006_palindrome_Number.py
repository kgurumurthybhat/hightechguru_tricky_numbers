# Solution in Python - Palindrome number
# (Brute force, think of improving this solution!)

import time


def main():
    biggest_palindrome = 0
    products = '0 X 0'

    for x in range(1000, 10000):
        for y in range(x, 10000):
            number_to_test = x * y
            if is_palindrome(number_to_test):
                if number_to_test > biggest_palindrome:
                    biggest_palindrome = number_to_test
                    products = "{} X {}".format(x, y)
    return biggest_palindrome, products


def is_palindrome(test):
    test = str(test)
    if test == test[::-1]:
        return True
    else:
        return False


start_time = time.time()
print(main())
print("Time taken {}".format(time.time() - start_time))