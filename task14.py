from random import randint


def partition(array, l, r):
    if l == r:
        return l

    pivot_ind = randint(l, r)
    array[pivot_ind], array[r] = array[r], array[pivot_ind]

    p, pivot = l, array[r]
    for i in range(l, r):
        if array[i] < pivot:
            if i != p:
                array[i], array[p] = array[p], array[i]
            p += 1
    array[p], array[r] = pivot, array[p]
    return p


def quick_sort_k(array, l, r, k):
    if l - r == 1:
        return array[0]
    p = partition(array, l, r)
    if k == p:
        return array[p]
    if k < p:
        return quick_sort_k(array, l, p - 1, k)
    else:
        return quick_sort_k(array, p + 1, r, k)


test = [3, 2, 1, 5, 6, 4]

kth = quick_sort_k(test, 0, len(test) - 1, 0)

print(kth)