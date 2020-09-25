"""
53. 最大子序和
难度 简单
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
示例:
输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""
from typing import List


class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        """时间O(n), 空间O(n), 使用数组保存代表以第i个数结尾的连续子数组的最大和"""
        b = nums[:]
        result = nums[0]
        for i in range(1, len(nums)):
            b[i] = max(b[i - 1] + nums[i], nums[i])
            if b[i] > result:
                result = b[i]
        return result


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """时间O(n), 空间O(1), 滚动数组"""
        result = nums[0]
        pre = nums[0]
        for i in range(1, len(nums)):
            pre = max(pre + nums[i], nums[i])
            if pre > result:
                result = pre
        return result


s = Solution()
n = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(s.maxSubArray(n))
