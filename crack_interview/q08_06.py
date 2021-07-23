from typing import List


class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """

        def han(n, A, B, C):
            if n == 1:
                C.append(A.pop())
                return
            han(n - 1, A, C, B)
            C.append(A.pop())
            han(n - 1, B, A, C)

        han(len(A), A, B, C)


if __name__ == '__main__':
    a = [6, 5, 4, 3, 2, 1, 0]
    b = []
    c = []
    s = Solution()
    s.hanota(a, b, c)
    print(a, b, c)
