"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        ans = []
        self.track_back(nums, [], ans)
        return ans

    def track_back(self, nums: List[int], tmp: List[int], ans: List[List[int]]):
        if len(tmp) == len(nums):
            ans.append(tmp[:])
        else:
            for num in nums:
                if num not in tmp:
                    tmp.append(num)
                    self.track_back(nums, tmp, ans)
                    tmp.pop(len(tmp) - 1)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    ans = s.permute(nums)
    print(ans)
    print(s.permute([0, 1]))
