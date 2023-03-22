from random import randint


def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp


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


def quick_sort(array, l, r):
    if r < l:
        return
    p = partition(array, l, r)
    quick_sort(array, l, p - 1)
    quick_sort(array, p + 1, r)


test = [randint(0, 100) for _ in range(16)]

print(test)

quick_sort(test, 0, len(test) - 1)

print(test)
