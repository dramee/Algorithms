from random import randint

test = [3, 2, 1]


def merge_and_cnt(array, left, mid, right):

    new_arr = [0] * (right - left)
    i = left
    j = mid
    k = 0
    inversions = 0

    while i < mid and j < right:
        if array[i] < array[j]:
            new_arr[k] = array[i]
            i += 1
        else:
            new_arr[k] = array[j]
            j += 1
            inversions += mid - i
        k += 1

    while i < mid:
        new_arr[k] = array[i]
        i += 1
        k += 1

    while j < right:
        new_arr[k] = array[j]
        j += 1
        k += 1

    for i in range(left, right):
        array[i] = new_arr[i - left]

    return inversions


def merge_sort_and_cnt(array, l, r):
    inversions = 0
    if r - l > 1:

        mid = l + (r - l) // 2

        inversions += merge_sort_and_cnt(array, l, mid)
        inversions += merge_sort_and_cnt(array, mid, r)
        inversions += merge_and_cnt(array, l, mid, r)
    return inversions


def sol_for_leet(arr):

    for i in range(len(arr)):
        if i - arr[i] > 1 or i - arr[i] < -1:
            return False

    return True


test1 = [5, 4, 3, 2, 1]
test2 = [1, 2, 3, 4, 5]

print(merge_sort_and_cnt(test1, 0, len(test1)))
print(merge_sort_and_cnt(test2, 0, len(test2)))

for i in range(16, 32):

    test = [randint(0, 50) for _ in range(i)]

    print(test)
    print(merge_sort_and_cnt(test, 0, i))
    input()


