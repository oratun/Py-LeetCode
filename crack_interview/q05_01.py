class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        M = M << i
        # 依次将i-j置为0
        for m in range(i, j + 1):
            a = ~(1 << m)
            N = N & a
        return N | M


if __name__ == '__main__':
    s = Solution()
    N = 2032243561
    M = 10
    i = 24
    j = 29
    print(s.insertBits(N, M, i, j))
