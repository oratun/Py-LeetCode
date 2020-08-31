"""
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。
示例：
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,
返回 13。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if k == 1:
            return matrix[0][0]
        m = 1  # matrix[i][j] 是第几小的元素
        n = len(matrix)
        i, j = 0, 0
        while i < n and j < n:
            if matrix[i][j + 1] <= matrix[j + 1][i]:
                i += 1
            else:
                j += 1
            m += 1
            if m == k:
                return matrix[i][j]


s = Solution()
a = s.kthSmallest([
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
], 8)
print(a)
