from test_framework import generic_test


def parity(x):
    # TODO - you fill in here.
    
    # MYSOLUTION 12 us
    # num_set_bits = 0
    # while x:
    #     if bin(x)[-1] == '1':
    #         num_set_bits += 1
    #     x >>= 1
    # return num_set_bits % 2

    # p27 solution #1 7us
    # result = 0
    # while x:
    #     result ^= x & 1
    #     x >>= 1
    # return result

    # p27solution #2 2us
    # result = 0
    # while x:
    #     result ^= 1 
    #     x &= x - 1 
    # return result

    # fastest p 29
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1 

if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
