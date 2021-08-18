from collections import defaultdict


class Solution:
    def countArrangement(self, n: int) -> int:
        match = defaultdict(list)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i % j == 0 or j % i == 0:
                    match[i].append(j)

        num = 0
        visited = set()

        def back_track(idx: int):
            if idx == n + 1:
                nonlocal num
                num += 1
                return
            for j in match[idx]:
                if j not in visited:
                    visited.add(j)
                    back_track(idx + 1)
                    visited.discard(j)

        back_track(1)
        return num


if __name__ == '__main__':
    s = Solution()
    print(s.countArrangement(15))
