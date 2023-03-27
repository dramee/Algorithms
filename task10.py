def radix_sort(array):

    length = len(array[0])

    for i in range(length - 1, -1, -1):
        buff = ["" for _ in range(len(array))]
        symbols = [0 for _ in range(128)]
        for j in range(len(array)):
            symbols[ord(array[j][i])] += 1

        for k in range(1, 128):
            symbols[k] += symbols[k - 1]

        for j in range(len(array) - 1, -1, -1):
            symbols[ord(array[j][i])] -= 1
            buff[symbols[ord(array[j][i])]] = array[j]

        array = buff.copy()

    return array


test = ["abdqdq", "ackfgd", "cd213a", "bdeqrq", "efeqwe"]

test = radix_sort(test)

print(test, sorted(test))
