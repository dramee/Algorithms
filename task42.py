from typing import List


class SegmentTree:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.n = end + 1
        self.seg = [0] * (self.n * 4)

    def getTotalLess(self, val):

        def query(ind, low, high, left, right):

            if high < left or low > right:
                return 0

            if low >= left and high <= right:
                return self.seg[ind]

            mid = (low + high) // 2
            leftAns = query(2 * ind + 1, low, mid, left, right)
            rightAns = query(2 * ind + 2, mid + 1, high, left, right)

            return leftAns + rightAns

        ans = query(0, self.start, self.end, self.start, val - 1)
        self.addValue(val)
        return ans

    def addValue(self, val):

        def update(ind, low, high, value):

            if low == high:
                self.seg[ind] += 1
                return

            mid = (low + high) // 2
            if low <= value <= mid:
                update(2 * ind + 1, low, mid, value)
            else:
                update(2 * ind + 2, mid + 1, high, value)

            self.seg[ind] = self.seg[2 * ind + 1] + self.seg[2 * ind + 2]

        update(0, self.start, self.end, val)


def countSmaller(nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [0] * n

    for i in range(n - 1, -1, -1):
        nums[i] += 10000

    mini, maxi = min(nums), max(nums)
    segTree = SegmentTree(mini, maxi)

    for i in range(n - 1, -1, -1):
        ans[i] = segTree.getTotalLess(nums[i])

    return ans
