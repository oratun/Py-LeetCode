from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """ part1: try topo sort by kahn """
        # 领接表表示
        adj = [[] for i in range(numCourses)]
        for [i, j] in prerequisites:
            adj[j].append(i)
        # 各顶点的入度
        in_degree = [0 for i in range(numCourses)]
        for i in adj:
            for j in i:
                in_degree[j] += 1

        queue = [i for i in range(numCourses) if in_degree[i] == 0]
        result = []
        while queue:
            i = queue.pop(0)
            result.append(i)
            for j in adj[i]:
                in_degree[j] -= 1
                if in_degree[j] == 0:
                    queue.append(j)
        if len(result) != numCourses:
            return []
        return result


if __name__ == '__main__':
    num = 3
    pre = [[1, 0], [1, 2], [0, 1]]
    s = Solution()
    r = s.findOrder(num, pre)
    print(r)
