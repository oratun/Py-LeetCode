'''
给你一个数组 nums和一个值 val，你需要 原地 移除所有数值等于val的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
示例 1:
给定 nums = [3,2,2,3], val = 3,
函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
你不需要考虑数组中超出新长度后面的元素。

示例2:
给定 nums = [0,1,2,2,3,0,4,2], val = 2,
函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
注意这五个元素可为任意顺序。
你不需要考虑数组中超出新长度后面的元素。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/all-about-array/x9p1iv/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = -1
        for j in range(0, len(nums)):
            if nums[j] != val:
                i += 1
                nums[i] = nums[j]
        return i + 1


s = Solution()
nums = [3, 2, 2, 3]
print(s.removeElement(nums, 3))
print(nums)

nums = [0, 1, 2, 2, 3, 0, 4, 2]
print(s.removeElement(nums, 2))
print(nums)
