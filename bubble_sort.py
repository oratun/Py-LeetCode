"""
冒泡排序
"""
from typing import List


def sort(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    if n < 2:
        return
    for i in range(n):
        flag = False  # 是否有交换
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                tmp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = tmp
                flag = True
        if not flag:
            break
