from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                # 左半侧有序
                if nums[left] == target:
                    return left
                if nums[left] < target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < nums[right]:
                # 右半侧有序
                if nums[right] == target:
                    return right
                if nums[right] >= target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


if __name__ == '__main__':
    s = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 6
    # nums = [3, 1]
    # target = 1
    # nums = [5, 1, 3]
    # target = 1
    print(s.search(nums, target))
