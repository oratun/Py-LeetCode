"""
搜索旋转排序数组
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        这里用二分法
        """
        left = 0
        right = len(nums) - 1

        def bin_search(nums: List[int], target: int, left: int, right: int):
            if right < left:
                return -1
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            # mid 左侧有序
            elif nums[left] <= nums[mid]:
                if nums[left] == target:
                    return left
                elif nums[left] < target < nums[mid]:
                    return bin_search(nums, target, left, mid - 1)
                else:
                    return bin_search(nums, target, mid + 1, right)
            elif nums[mid] <= nums[right]:
                if nums[right] == target:
                    return right
                elif nums[mid] < target < nums[right]:
                    return bin_search(nums, target, mid + 1, right)
                else:
                    return bin_search(nums, target, left, mid - 1)
            return -1

        return bin_search(nums, target, left, right)


if __name__ == '__main__':
    s = Solution()
    print(s.search([3,1], 4))
