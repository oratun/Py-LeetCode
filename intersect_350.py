"""
350. 两个数组的交集 II
给定两个数组，编写一个函数来计算它们的交集。
示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
示例 2:
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]
说明：
输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
我们可以不考虑输出结果的顺序。
进阶：
如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
"""
from typing import List


class Solution:
    # 未排序
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = {}
        for i in nums1:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        inter = []
        for j in nums2:
            if j in a and a[j] > 0:
                inter.append(j)
                a[j] -= 1
        return inter

    # 排序版
    def intersect_sort(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        inter = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                inter.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return inter


s = Solution()
intersect = s.intersect_sort

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersect(nums1, nums2))

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersect(nums1, nums2))

nums1 = [2, 1]
nums2 = [1, 1]
print(intersect(nums1, nums2))
