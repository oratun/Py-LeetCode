"""
排序
"""
from typing import List


def bubble_sort(nums: List[int]):
    """"""
    if len(nums) <= 1:
        return nums
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


def quick_sort(nums: List[int]):
    """"""
    pivot = nums[0]


def partion(nums: List[int]):
    """"""



if __name__ == '__main__':
    nums = [3, 2, 1, 5, 4, ]
    # print(bubble_sort(nums))
    print(quick_sort(nums))
