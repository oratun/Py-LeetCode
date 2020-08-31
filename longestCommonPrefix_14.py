"""
14. 最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
示例 1:
输入: ["flower","flow","flight"]
输出: "fl"
示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:
所有输入只包含小写字母 a-z 。
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        if not strs:
            return prefix
        flag = True
        for i in range(len(strs[0])):
            c = strs[0][i]
            for s in strs[1:]:
                if len(s) <= i or s[i] != c:
                    flag = False
                    break
            if not flag:
                break
            prefix += c
        return prefix


s = Solution()
for s_list in [
    ["flower", "flow", "flight"],
    ["dog", "racecar", "car"],
    ["aa", "a"],
]:
    print(s.longestCommonPrefix(s_list))
