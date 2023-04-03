from random import randint


def merge(array, l1, r1, l2, r2, buff_ind):

    while l1 < r1 and l2 < r2:
        if array[l1] < array[l2]:
            array[l1], array[buff_ind] = array[buff_ind], array[l1]
            l1 += 1
        else:
            array[l2], array[buff_ind] = array[buff_ind], array[l2]
            l2 += 1
        buff_ind += 1

    while l1 < r1:
        array[l1], array[buff_ind] = array[buff_ind], array[l1]
        l1 += 1
        buff_ind += 1

    while l2 < r2:
        array[l2], array[buff_ind] = array[buff_ind], array[l2]
        l2 += 1
        buff_ind += 1


def merge_sort_impl(array, l, r, buff_ind):
    if r - l > 1:

        mid = l + (r - l) // 2

        merge_sort_inplace(array, l, mid)
        merge_sort_inplace(array, mid, r)
        merge(array, l, mid, mid, r, buff_ind)
    else:
        array[l], array[buff_ind] = array[buff_ind], array[l]


def merge_sort_inplace(array, l, r):

    if r - l > 1:
        m = l + (r - l) // 2
        buffer = l + r - m

        merge_sort_impl(array, l, m, buffer)

        while buffer - l > 2:
            n = buffer
            buffer = l + (n - l + 1) // 2
            merge_sort_impl(array, buffer, n, l)
            merge(array, l, l + n - buffer, n, r, buffer)

        n = buffer
        while n > l:
            m = n
            while m < r and array[m] < array[m - 1]:
                array[m], array[m - 1] = array[m - 1], array[m]
                m += 1
            n -= 1


for i in range(128, 2 ** 12):
    test1 = [randint(0, 1000) for _ in range(i)]
    test2 = test1.copy()
    test2.sort()

    merge_sort_inplace(test1, 0, i)

    assert test1 == test2
