test_arr = [91, 56, 183, 8, 47, 140, 136, 191, 92, 47, 136, 178, 106, 87, 153, 39, 38, 121, 137, 148, 19, 156, 117,
            84, 84, 152, 54, 142, 157, 136, 13, 83, 152, 40, 176, 162, 79, 21, 145, 20, 129, 3, 195, 10, 42, 160, 150,
            49, 193, 56]

test_arr2 = [4, 5, 6, 1, 2, 3, 23, 1, 123, 31, 3213, 123, 21, 12]


def merge(arr, start1, end1, end2):
    start2 = end1 + 1

    if arr[end1] <= arr[start2]:
        return

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


def merge_sort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2

        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)

        merge(arr, l, m, r)


merge_sort(test_arr2, 0, len(test_arr2) - 1)
print(test_arr2)

