test_arr2 = [4, 3, 2, 1]


def merge_and_cnt(arr, start1, end1, end2):
    start2 = end1 + 1
    k = 0
    if arr[end1] <= arr[start2]:
        return 0

    while start1 <= end1 and start2 <= end2:

        if arr[start1] <= arr[start2]:
            start1 += 1
        else:
            value = arr[start2]
            index = start2

            while index != start1:
                arr[index] = arr[index - 1]
                index -= 1

            arr[start1] = value

            start1 += 1
            end1 += 1
            start2 += 1
            k += (end1 - start1 + 1)
    return k


def merge_sort_and_cnt(arr, l, r):
    t1 = t2 = t3 = 0
    if l < r:
        m = l + (r - l) // 2

        t1 = merge_sort_and_cnt(arr, l, m)
        t2 = merge_sort_and_cnt(arr, m + 1, r)

        t3 = merge_and_cnt(arr, l, m, r)
    return t1 + t2 + t3


def sol_for_leet(arr):

    for i in range(len(arr)):
        if i - arr[i] > 1 or i - arr[i] < -1:
            return False

    return True