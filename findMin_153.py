"""
153. 寻找旋转排序数组中的最小值
难度 中等
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
请找出其中最小的元素。
你可以假设数组中不存在重复元素。
示例 1:
输入: [3,4,5,1,2]
输出: 1
示例 2:
输入: [4,5,6,7,0,1,2]
输出: 0
"""
from typing import List


class Solution1:
    def findMin(self, nums: List[int]) -> int:
        """遍历法 时间复杂度O(n)"""
        j = 0
        n = len(nums)
        if n == 0:
            return
        elif n == 1:
            return nums[0]
        while j < n - 1:
            if nums[j] > nums[j + 1]:
                break
            j += 1
        if j == n - 1:
            return nums[0]
        return nums[j + 1]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """二分"""
        n = len(nums)
        start = 0
        end = n - 1
        mid = (start + end) // 2
        if nums[start] < nums[end]:
            return nums[start]
        while start < end:
            if nums[mid] > nums[start]:
                start = mid
            elif nums[mid] < nums[start]:
                end = mid
            else:
                break
            mid = (start + end) // 2
        if nums[start] > nums[end]:
            return nums[end]
        return nums[start]


s = Solution()
for nums in [
    [3, 4, 5, 1, 2],
    [4, 5, 6, 7, 0, 1, 2],
    [4, 5, 0, 1, 2],
    [1, 2],
    [1],
    [1, 2, 3]
]:
    print(s.findMin(nums))
