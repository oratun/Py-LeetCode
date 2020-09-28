"""
300. 最长上升子序列
难度 中等
给定一个无序的整数数组，找到其中最长上升子序列的长度。
示例:
输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:
可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """动态规划"""
        if not nums:
            return 0
        b = nums[:]  # b[i]表示以nums[i]结尾的最长上升子序列的长度
        b[0] = 1
        result = 1
        min_val = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= min_val:  # nums[0:i]都比nums[i]大
                min_val = nums[i]
                b[i] = 1
                continue
            max_ = 0  # nums[0:i]存在比nums[i]小的值，b[0:i]中的最大长度
            for j in range(0, i):
                if nums[j] < nums[i] and b[j] > max_:
                    max_ = b[j]
            b[i] = max_ + 1
            if b[i] > result:
                result = b[i]
        return result


s = Solution()
for nums in [[10, 9, 2, 5, 3, 7, 101, 18], [4, 10, 4, 3, 8, 9]]:
    print(s.lengthOfLIS(nums))
