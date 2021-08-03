from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        # 每个位置左边高度的最大值
        left_max = [0] * len(height)
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i])
        right_max = [0] * len(height)
        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        total = 0
        for i in range(len(height)):
            water = min(left_max[i], right_max[i]) - height[i]
            if water > 0:
                total += water
        return total


if __name__ == '__main__':
    s = Solution()
    height = [4, 2, 0, 3, 2, 5]
    s.trap(height)
