"""
1. 两数之和
难度 简单
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""
from typing import List


class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """暴力解法"""
        n = len(nums)
        if n == 0:
            return []
        res = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return res


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """哈希，两次遍历"""
        a = {}
        for i, val in enumerate(nums):
            if val in a:
                a[val].append(i)
            else:
                a[val] = [i]
        for val in a:
            if target - val in a:
                if target - val != val:
                    return [a[val][0], a[target - val][0]]
                if len(a[val]) > 1:
                    return [a[val][0], a[val][1]]
        return []


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """哈希,一次遍历"""
        a = {}
        for i, val in enumerate(nums):
            if val in a:
                a[val].append(i)
            else:
                a[val] = [i]
            if val in a and target - val in a:
                if target - val != val:
                    return [a[target - val][0], a[val][0]]
                if len(a[val]) > 1:
                    return [a[val][0], a[val][1]]
        return []


s = Solution()
for nums, target in [
    ([2, 7, 11, 15], 9),
    ([3, 2, 4], 6),
    ([-3, 4, 3, 90], 0),
    ([3, 3], 6),
]:
    print(s.twoSum(nums, target=target))
