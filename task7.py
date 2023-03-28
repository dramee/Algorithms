from random import randint


def merge(array, start1, end1, start2, end2, buff_ind):

    # merge two parts 'till don't go to the of the edges
    while start1 < end1 and start2 < end2:

        if array[start1] < array[start2]:
            array[buff_ind], array[start1] = array[start1], array[buff_ind]
            start1 += 1
            buff_ind += 1
        else:
            array[buff_ind], array[start2] = array[start2], array[buff_ind]
            start2 += 1
            buff_ind += 1

    # complete merge if not all elements went into buffer
    while start1 < end1:
        array[start1], array[buff_ind] = array[buff_ind], array[start1]
        start1 += 1
        buff_ind += 1

    while start2 < end2:
        array[start2], array[buff_ind] = array[buff_ind], array[start2]
        start2 += 1
        buff_ind += 1

def sort_range(array, l, r, buff_ind):

    mid = l + (r - l) // 2

    sort_range(array, l, mid, buff_ind)
    sort_range(array,)


def merge_sort_inplace(array, l, r):
    if r - l - 1 <= 1:
        return

    # if r - l - 1 == 2:
    #     if array[l] > array[r]:
    #         array[l], array[r] = array[r], array[l]

    else:

        unsorted = l + (r - l) // 2

        buff = unsorted
        if (r - l) % 2 == 1:
            buff += 1

        mid = l + (unsorted - l) // 2
        merge_sort_inplace(array, l, mid)
        merge_sort_inplace(array, mid, unsorted)
        merge(array, l, mid, mid, unsorted, buff)
        print(array)

        unsorted = buff
        while unsorted - l >= 2:
            mid = l + (unsorted - l) // 2

            buff = mid
            if (unsorted - l) % 2 == 1:
                buff += 1

            merge_sort_inplace(array, l, mid)
            merge(array, l, mid, unsorted, r, buff)
            print(array)

            unsorted = buff

    i = 0
    while l + i + 1 < r and array[l + i] > array[l + i + 1]:
        array[l + i], array[l + i + 1] = array[l + i + 1], array[l + i]
        i += 1

    i = 0
    # while r - i - 1 > l and array[r - i] < array[r - i - 1]:
    #     array[r - i], array[r - i - 1] = array[r - i - 1], array[r - i]
    #     i += 1

# # l, mid, mid + 1, r,buff,nums
# def merge(l1, r1, buff_l, buff_r, l2, r2, nums, is_merge_buff):
#     # лев сортнут, буффер сортнут,правый нет
#     # сливаем левый с буфером, используя как буфер средний и буфер
#     # [l2,r2] может быть на 1 длиньше [l1,r1]
#     i, j, k = l1, buff_l, l2
#     while i <= r1 and j <= buff_r:
#         if nums[i] < nums[j]:
#             nums[i], nums[k] = nums[k], nums[i]
#             i += 1
#         else:
#             nums[j], nums[k] = nums[k], nums[j]
#             j += 1
#         k += 1
#     while i <= r1:
#         nums[i], nums[k] = nums[k], nums[i]
#         i += 1
#         k += 1
#     if is_merge_buff:
#         while j <= buff_r:
#             nums[j], nums[k] = nums[k], nums[j]
#             j += 1
#             k += 1
#
#
# def merge_sort(l1, r1, l2, r2, nums):
#     # сорчу [l1,r1] используя [l2,r2] буфером.
#     # [l2,r2](r2-1) должен стат сортнутым и поменяться местами с [l1,r1]
#     # буфер может быть на 1 длиньше массива
#     if r1 - l1 + 1 < 1:
#         return
#     if r1 - l1 + 1 == 1:
#         nums[l1], nums[l2] = nums[l2], nums[l1]
#         return
#     if r1 - l1 + 1 == 2:
#         if nums[l1] > nums[r1]:
#             nums[l1], nums[r1] = nums[r1], nums[l1]
#         return
#     mid = (l1 + r1) // 2
#     merge_sort(l1, mid, l2, r2, nums)
#     merge_sort(mid + 1, r1, l2, r2, nums)
#     merge(l1, mid, mid + 1, r1, l2, r2, nums, True)  # [l1,mid],[mid+1,r1] сортнуты
#     i, j = l1, l2
#     while i <= r1:
#         nums[i], nums[j] = nums[j], nums[i]
#         i += 1
#         j += 1
#     # поменялись местами возвращаю в исходные
#     # в итоге получаю сортнутый [l1,mid]
#
#
# def sort(l, r, buff_l, buff_r, nums):
#     if l > r:
#         return
#     if l == r:  # буффер(сортированный) это массив без левого эл-та, nums[0] -тот самый
#         tmp = nums[0]
#         i = 1
#         while i < len(nums) and tmp > nums[i]:
#             nums[i - 1] = nums[i]
#             i += 1
#         nums[i - 1] = tmp
#         return
#     mid = (l + r) // 2  # длины лев и сред равны или длина лев на 1 больше
#     fl = (mid - l + 1) > (r - (mid + 1) + 1)
#     merge_sort(mid + 1, r, l, mid, nums)  # сорчу [mid+1,r] используя [l,mid] буфером.
#     i, j = l, mid + 1
#     while j <= r:
#         nums[i], nums[j] = nums[j], nums[i]
#         i += 1
#         j += 1
#     # [l,mid](mid-1) должен стат сортнутым
#     if fl:  # если лев был длинее прав, то по сути я меняю длины местами
#         mid -= 1
#     fl2 = (r - (mid + 1) + 1) > (mid - l + 1)
#     merge(l, mid, buff_l, buff_r, mid + 1 + fl2, r, nums, False)  # лев сортнут, серединный нет,буффер сортнут
#     # сливаем левый с буфером, используя как буфер средний и буфер
#     sort(l, mid + fl, mid + 1 + fl, buff_r, nums)  # идём рекурсивно 2 два раза уменьшая длину...
#
#
# def sort_array(nums):
#     l, r, buff = 0, len(nums) - 2, len(nums) - 1  # буффер из одного эл-та
#     sort(l, r, buff, buff, nums)


test = [randint(0, 200) for _ in range(8)]

merge_sort_inplace(test, 0, len(test))

print(test)
