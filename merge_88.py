"""
88. 合并两个有序数组
难度 简单
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
说明:
初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:
输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
输出: [1,2,2,3,5,6]
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 倒序遍历
        i, j = m - 1, n - 1
        k = m + n - 1
        while i > -1 and j > -1:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            elif j > -1:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j > -1:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


s = Solution()
for nums1, m, nums2, n in [
    [[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3],
    [[0], 0, [1], 1],
    [[2, 0], 1, [1], 1],
    [[4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3],
    [[1], 1, [], 0],
]:
    s.merge(nums1, m, nums2, n)
    print(nums1)
