from random import randint


def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp


def flag(array):
    i = k = 0
    j = len(array) - 1
    while k <= j and i < len(array):
        if array[k] == 0:
            swap(array, i, k)
            i += 1
        elif array[k] == 2:
            swap(array, j, k)
            j -= 1
        else:
            k += 1


test = [randint(0, 2) for _ in range(128)]
print(test)

flag(test)

print(test)

