arr = [0]


def can_jump(nums):

    pos = 0

    while pos < len(nums):

        max_jump = nums[pos]

        if pos != len(nums) - 1 and max_jump == 0:
            return False

        m = 0
        new_pos = pos
        for i in range(pos, pos + nums[pos] + 1):

            if i + nums[i] >= len(nums) - 1:
                return True

            if i + nums[i] != 0:
                if i + nums[i] > m:
                    m = i + nums[i]
                    new_pos = i

        if pos == new_pos:
            return False

        pos = new_pos


print(can_jump(nums=arr))
