"""
15. 三数之和
难度 中等
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。
示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
from typing import List


class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """[[-1, 0, 1], [-1, 2, -1], [0, 1, -1]]"""
        n = len(nums)
        if n < 3:
            return []
        res = []
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for c in nums[j + 1:]:
                    if nums[i] + nums[j] + c == 0:
                        res.append([nums[i], nums[j], c])
        return res


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """"""
        n = len(nums)
        res = []
        # 从小到大排序
        nums.sort()
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            k = n - 1
            target = -nums[i]
            for j in range(i + 1, n - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                while k > j and nums[j] + nums[k] > target:
                    k -= 1
                if j == k:
                    break
                if nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
        return res


class Solution3:
    """官方题解"""

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()

        # 枚举 a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
            # 枚举 b
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans


s = Solution()
# [-4, -1, -1, 0, 1, 2]
# [-2,-1,0,1,2,3]
for nums in [[-1, 0, 1, 2, -1, -4],
             [1, -1, -1, 0],
             [3, 0, -2, -1, 1, 2], ]:
    print(s.threeSum(nums))
