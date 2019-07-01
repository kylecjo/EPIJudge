from test_framework import generic_test


def power(x, y):
    # TODO - you fill in here.
    # my brute force solution
    print(x, y)
    result = x
    for i in range(1, y):
        print('y: ', y)
        result *= x
        print('result: ', result)

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_x_y.py", 'power_x_y.tsv', power))
