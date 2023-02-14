a = [12, 32, 35, 41, 52, 67, 90, 112, 131, 315, 123]


def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        curr_ind = (left + right) // 2
        if nums[curr_ind] == target:
            return curr_ind
        elif nums[curr_ind] < target:
            left = curr_ind + 1
        else:
            right = curr_ind - 1
    return -1


print(search(a, 41))
