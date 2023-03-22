from random import randint


def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp


def flag(array):
    i = k = 0
    j = len(array) - 1
    while k <= j:
        if array[k] == 0:
            swap(array, i, k)
            i += 1
            k += 1
        elif array[k] == 2:
            swap(array, j, k)
            j -= 1
        else:
            k += 1


test = [2, 0, 2, 1, 1, 0]
print(test)

flag(test)

print(test)

