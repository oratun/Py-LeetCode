"""
全排列2
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """"""
        nums.sort()
        ret = []

        def permute(nums: List[int], tmp: List[int]):
            if len(nums) == 0:
                ret.append(tmp)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                k = nums[i]
                permute(nums[0:i] + nums[i + 1:], tmp[:] + [k])

        permute(nums, [])
        return ret


if __name__ == '__main__':
    s = Solution()
    for nums in [
        [1,2],
        [1, 1, 2],
        [1, 2, 3],
    ]:
        print(s.permuteUnique(nums))
