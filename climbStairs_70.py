"""
假设你正在爬楼梯。需要 n阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution1:
    step_dict = {}

    def climbStairs(self, n: int) -> int:
        """"""
        if n == 1:
            self.step_dict[1] = 1
            return 1
        if n == 2:
            self.step_dict[2] = 2
            return 2
        if n - 1 in self.step_dict:
            a = self.step_dict[n - 1]
        else:
            a = self.climbStairs(n - 1)
            self.step_dict[n - 1] = a
        if n - 2 in self.step_dict:
            b = self.step_dict[n - 2]
        else:
            b = self.climbStairs(n - 2)
            self.step_dict[n - 2] = b
        return a + b


class Solution:
    def climbStairs(self, n: int) -> int:
        """斐波那契 滚动数组"""
        p, q, r = 0, 0, 1
        for i in range(n):
            p = q
            q = r
            r = p+q
        return r


s = Solution()
for m in [2, 3, 38]:
    print(s.climbStairs(m))
