from test_framework import generic_test
from math import floor, log10

def is_palindrome_number(x):
    # TODO - you fill in here.
    if x <= 0:
        return x == 0
    
    num_digits = floor(log10(x)) + 1
    MSB_MASK = 10 ** (num_digits -1)

    for i in range(num_digits // 2):
        if x // MSB_MASK != x % 10:
            return False
        x %= MSB_MASK
        x //= 10

        MSB_MASK //= 100  
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_number_palindromic.py",
                                       "is_number_palindromic.tsv",
                                       is_palindrome_number))
