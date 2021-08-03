from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        if len(nums) == 1:
            return nums[0] == target
        left = 0
        right = len(nums) - 1
        while nums[left] == nums[right] and right >0:
            right -= 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            # 左半部分有序
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 右半部分有序
            elif nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


if __name__ == '__main__':
    s = Solution()
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 7
    nums = [1, 1]
    target = 1
    print(s.search(nums, target))
