"""
数组中的第K个最大元素
"""
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        借助快速排序思想
        1. 选取基准点
        2. 按照基准点进行分区, O(n)
        3. 比较 k 和 基准点的位置，判断所属区间
        """

        def quick_find(nums: List[int], p: int, q: int):
            # p、q 待处理区间
            # 选取基准点 pivot  [3,2,1,5,6,4]
            nonlocal k
            pivot = nums[q]
            i = p
            for j in range(p, q + 1):
                if nums[j] > pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[q] = nums[q], nums[i]
            if i + 1 == k:
                return nums[i]
            if i + 1 > k:
                return quick_find(nums, p, i - 1)
            return quick_find(nums, i + 1, q)

        return quick_find(nums, 0, len(nums) - 1)

    def findKthLargestByStack(self, nums: List[int], k: int) -> int:
        """
        使用最大堆
        """

