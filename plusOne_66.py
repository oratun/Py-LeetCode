"""
66. 加一
难度 简单
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
示例 1:
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:
输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        i = n - 1
        expand = True  # 是否需要扩展数组，满足进位
        while i >= 0:
            if digits[i] < 9:
                digits[i] += 1
                expand = False
                break
            digits[i] = 0
            i -= 1
        if expand:
            digits = [1] + digits
        return digits


s = Solution()
d_list = [
    [1, 2, 3],
    [4, 3, 2, 1],
    [9, 9],
    [0]
]
for d in d_list:
    print(s.plusOne(d))
