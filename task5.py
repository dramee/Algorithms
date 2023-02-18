data = [1231, 312, 31, 131, 3135, 3151, 32]


def insertion_sort_k(array, k):
    for i in range(k - 1, len(array)):
        j = i
        while j - k >= 0 and array[j - k] > array[j]:
            array[j - k] += array[j]
            array[j] = array[j - k] - array[j]
            array[j - k] = array[j - k] - array[j]
            j -= k
    pass


def shell_sort(array):
    seq = [1750, 701, 301, 132, 57, 23, 10, 4, 1]
    for num in seq:
        insertion_sort_k(array, num)
    pass


def hIndex(self, citations: List[int]) -> int:
    shell_sort(citations)
    citations.reverse()

    for i in range(len(citations)):
        if citations[i] <= i:
            return i
    return len(citations)
