from test_framework import generic_test


def reverse(x):
    # TODO - you fill in here.
    result = 0
    x_remaining = abs(x)
    while x_remaining:
        result = result * 10 + x_remaining % 10 
        x_remaining = x_remaining // 10 
    if x_remaining not in range(-pow(2, 31), pow(2, 31)):
        return 0    
    if x < 0:
        return result * -1
    else: 
        return result



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_digits.py",
                                       'reverse_digits.tsv', reverse))
