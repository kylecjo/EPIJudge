from test_framework import generic_test


def count_bits(x):
    # TODO - you fill in here.
    
    # MYSOLUTION
    # num_bits = 0
    # while int(x) != 0:
    #     x_bin = bin(x)[2:]
    #     if x_bin[-1] == '1':
    #         num_bits += 1
    #     x = x >> 1

    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1

    return num_bits


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("count_bits.py", 'count_bits.tsv',
                                       count_bits))
