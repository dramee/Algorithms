def swap(array, i, j):

    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp


def merge(array, start1, end1, start2, end2, buff_start):

    while start1 < end1 and start2 < end2:
        if array[start1] < array[start2]:
            swap(array, start1, buff_start)
            start1 += 1
            buff_start += 1
        else:
            swap(array, start2, buff_start)
            start2 += 1
            buff_start += 1

    while start1 < end1:
        swap(array, start1, buff_start)
        start1 += 1
        buff_start += 1

    while start2 < end2:
        swap(array, start2, buff_start)
        start2 += 1
        buff_start += 1


