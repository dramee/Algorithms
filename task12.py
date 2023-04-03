from random import randint


def partition(array, left, right):
    if left == right:
        return left, left

    pivot_ind = randint(left, right)
    array[pivot_ind], array[right] = array[right], array[pivot_ind]

    pivot = array[right]
    l, h, c = left, left, left

    while c < right:

        if array[c] < pivot:
            tmp = array[c]
            array[c] = array[h]
            array[h] = array[l]
            array[l] = tmp
            l += 1
            h += 1

        elif array[c] == pivot:
            array[c], array[h] = array[h], array[c]
            h += 1

        c += 1

    array[right], array[h] = array[h], array[right]

    return l, h


def quick_sort(array, left, right):
    if right < left:
        return

    l, h = partition(array, left, right)

    quick_sort(array, left, l - 1)
    quick_sort(array, h + 1, right)


for i in range(512, 1024):
    test = [randint(0, 2000) for _ in range(i)]
    test_copy = test.copy()

    quick_sort(test, 0, len(test) - 1)
    test_copy.sort()

    assert test_copy == test