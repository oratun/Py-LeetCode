"""括号 22"""
from typing import List


class Solution:
    def generateParenthesis_v1(self, n: int) -> List[str]:
        """暴力生成所有组合+判断是否合法"""
        ans = []

        def generate(tmp: List):
            if len(tmp) == 2 * n:
                if valid(tmp):
                    ans.append(''.join(tmp))
                return
            generate(tmp[:] + ['('])
            generate(tmp[:] + [')'])

        def valid(tmp: List[str]):
            balence = 0
            for i in tmp:
                if i == '(':
                    balence += 1
                else:
                    balence -= 1
                if balence < 0:
                    return False
            if balence == 0:
                return True
            return False

        generate([])
        return ans

    def generateParenthesis_v2(self, n: int) -> List[str]:
        """在v1基础上改进"""
        ans = []

        def generate(tmp: List, balence: int):
            if balence < 0 or len(tmp) > 2 * n:
                return
            if len(tmp) == 2 * n and balence == 0:
                ans.append(''.join(tmp))
                return
            generate(tmp[:] + ['('], balence + 1)
            generate(tmp[:] + [')'], balence - 1)

        generate([], 0)
        return ans

    def generateParenthesis_v3(self, n: int) -> List[str]:
        """左括号数量小于n，则放左括号；左括号数量大于右括号，放右括号"""
        ans = []

        def generate(tmp: List, left: int, right: int):
            if len(tmp) == 2 * n:
                ans.append(''.join(tmp))
            if left < n:
                generate(tmp[:] + ['('], left + 1, right)
            if left > right:
                generate(tmp[:] + [')'], left, right + 1)

        generate([], 0, 0)
        return ans


if __name__ == '__main__':
    s = Solution()
    for i in [1, 3]:
        print(s.generateParenthesis_v3(i))
