from test_framework import generic_test


# my solution 2us
# def swap_bits(x, i, j):
#     # TODO - you fill in here.
#     BIT_MASK1 = 1 << i
#     BIT_MASK2 = 1 << j
#     i_bit = BIT_MASK1 & x
#     j_bit = BIT_MASK2 & x
#     if not (i_bit == 0 and j_bit == 0) and not (i_bit != 0 and j_bit != 0) :
#         x ^= 1 << j
#         x ^= 1 << i
#     return x

# book solution more succint 1us
def swap_bits(x, i, j):
    if (x >> i) & 1 != (x >> j) & 1:
        bit_mask = (1 << i) | ( 1 << j)
        x ^= bit_mask
    return x



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("swap_bits.py", 'swap_bits.tsv',
                                       swap_bits))
