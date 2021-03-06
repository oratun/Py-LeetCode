"""
189. 旋转数组
难度 简单
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
示例 1:
输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:
输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释:
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
说明:
尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的 原地 算法。
"""
from typing import List


class Solution:
    def reverse(self, nums: List[int], m: int, n: int) -> None:
        """
        反转数组，原地修改
        :param n: 终点索引
        :param m: 起点索引
        :param nums:
        :return:
        """
        for i in range(m, m + (n - m) // 2 + 1):
            t = nums[i]
            nums[i] = nums[n + m - i]
            nums[n + m - i] = t

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)


class Solution2:
    """方法二：环状"""

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        count = 0
        for start in range(n):
            cur = start
            prev = nums[cur]
            while True:
                next_ = (cur + k) % n
                tmp = nums[next_]
                nums[next_] = prev
                prev = tmp
                cur = next_
                count += 1
                if cur == start:
                    break
            if count == n:
                break


s = Solution2()
b = [1, 2, 3, 4, 5, 6, 7]
'''
[1, 2, 3, 1, 5, 6, 7] tmp =4
[1, 2, 3, 1, 5, 6, 4] tmp =7
[1, 2, 7, 1, 5, 6, 4] tmp =3
[1, 2, 7, 1, 5, 3, 4] tmp =6
[1, 6, 7, 1, 5, 3, 4] tmp =2
[1, 6, 7, 1, 2, 3, 4] tmp =5
[5, 6, 7, 1, 2, 3, 4] tmp =
'''
s.rotate(b, 3)
print(b)

c = [-1, -100, 3, 99]
s.rotate(c, 2)
print(c)
