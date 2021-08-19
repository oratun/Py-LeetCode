"""
48 旋转数组
1  2  3  4
5  6  7  8
9  10 11 12
13 14 15 16
变换过程：
matrix[i][j] -> matrix[j][n-1-i]
matrix[j][n-1-i] -> matrix[n-1-i][n-1-j]
matrix[n-1-i][n-1-j] -> matrix[n-1-j][i]
matrix[n-1-j][i] -> matrix[i][j]
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n % 2 == 0:
            m = k = n // 2
        else:
            m = (n + 1) // 2
            k = (n - 1) // 2
        for i in range(m):
            for j in range(k):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = tmp


if __name__ == '__main__':
    s = Solution()
    ma = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s.rotate(ma)
    print(ma)
