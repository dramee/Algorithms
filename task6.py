from task5 import shell_sort


def wiggle_sort(nums):
    shell_sort(nums)

    length = len(nums)

    nums1 = nums[:length // 2 + length % 2][::-1]
    nums2 = nums[length // 2 + length % 2:][::-1]

    for i in range(length):
        if i % 2 == 0:
            nums[i] = nums1[i // 2]
        else:
            nums[i] = nums2[i // 2]
    pass