fst_num, sec_num = map(int, input().split())


def divide(x, y):
    str_x = str(x)  # m := len x
    str_y = str(y)  # n := len y
    res = 0
    len_y = len(str_y)  # O(n) ops
    while x >= y:  # (m - n + 2) times
        curr_len = len_y  # m - n + 1
        sub_x = int(str_x[:curr_len])  # (m - n + 1) * O(n)
        if sub_x < y:  # m - n + 1
            curr_len += 1   # m - n + 1
            sub_x = int(str_x[:curr_len])  # (m - n + 1) * O(n)
        i = 1
        while (i * y <= sub_x) and (i < 10):  # (m - n + 1) * 10
            i += 1  # (m - n + 1) * 9
        res = res * 10 + i - 1  # 4 * (m - n + 1)
        sub_x = sub_x - (i - 1) * y  # 4 * (m - n + 1)
        str_x = str(sub_x) + str_x[curr_len:]  # O(n) + O(m - n) + O(n) + O(m - n - 1) + O(n) + O(m - n - 2) + ...
        #  + O(n) - O(n)
        x = int(str_x)
    return res


print(divide(fst_num, sec_num))  # in 11 and 14 string O(m*n)
