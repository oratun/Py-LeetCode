"""
最大子序和 53
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """"""
        pre = max_sub = nums[0]
        for i in range(1, len(nums)):
            current = max(nums[i], nums[i] + pre)
            if current > max_sub:
                max_sub = current
            pre = current
        return max_sub


if __name__ == '__main__':
    s = Solution()
    for nums in [
        [1], [0], [-1], [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [-10000],
    ]:
        print(s.maxSubArray(nums))
