from random import randint

# num1, num2 = map(int, input().split())


def num_len(x):
    length = 1 if x == 0 else 0
    while x:
        x //= 10
        length += 1
    return length


def sub_num(x, length=None):
    if length is None:
        length = num_len(x)
    half = int(length / 2 + 0.5)
    res1 = x // (10 ** half)
    res2 = x % (10 ** half)
    return res1, res2


def karatsuba(x, y):
    len_x = num_len(x)
    len_y = num_len(y)
    length = max(len_x, len_y)
    if length > 1:
        a, b = sub_num(x, length)
        c, d = sub_num(y, length)
        tmp1 = karatsuba(a, c)
        tmp2 = karatsuba(b, d)
        tmp3 = karatsuba(a + b, c + d)
        res = tmp1 * (10 ** (length + length % 2)) + ((tmp3 - tmp2 - tmp1) * (10 ** (length // 2 + length % 2))) + tmp2
        return res
    else:
        return x * y


def check(x, y):
    assert x * y == karatsuba(x, y)
    pass


for i in range(20):
    k = randint(10 ** 20, 10 ** 30)
    t = randint(10 ** 20, 10 ** 30)
    check(k, t)

check(314151321731131241, 12312312327162313123123132716923123129371)
check(1231301234, 312312312323123)
check(21, 2131237162941978426127931798641725610538615601379519)
