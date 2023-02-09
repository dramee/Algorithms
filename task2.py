from random import randint


# fst_num, sec_num = map(int, input().split())


def karatsuba(x, y):
    str_x = str(x)
    str_y = str(y)
    len_x = len(str_x)
    len_y = len(str_y)
    length = max(len_x, len_y)
    if length != 1:
        if length % 2 != 0:
            length += 1
        str_x = "0" * (length - len_x) + str_x
        str_y = "0" * (length - len_y) + str_y
        ind = length // 2
        a = int(str_x[:ind])
        b = int(str_x[ind:])
        c = int(str_y[:ind])
        d = int(str_y[ind:])
        tmp1 = karatsuba(a, c)
        tmp2 = karatsuba(b, d)
        tmp3 = karatsuba(a + b, c + d)
        res = tmp1 * 10 ** length + (tmp3 - tmp1 - tmp2) * 10 ** ind + tmp2
    else:
        res = x * y
    return res


# print(karatsuba(fst_num, sec_num))


def check(x, y):
    assert x * y == karatsuba(x, y)


for i in range(10):
    check(randint(10 ** 10, 10**20), randint(10 ** 10, 10**20))

