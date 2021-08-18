"""
拓扑排序
"""
from typing import List


class Graph:
    def __init__(self, v: int):
        """
        领接表表示图
        :param v: 顶点个数
        """
        self.v = v
        self.adj = [[] for i in range(v)]

    def add_edge(self, s: int, t: int):
        """
        新增一条顶点s到顶点t的边
        :param s:
        :param t:
        :return:
        """
        self.adj[s].append(t)

    def topo_sort_by_kahn(self):
        """
        kahn算法：找出一个入度为0的顶点，将其输出到结果中，然后将该节点可达的节点的入度都减1。
        :return:
        """
        in_degree: List[int] = [0] * self.v
        for i in self.adj:
            for j in i:
                in_degree[j] += 1
        queue: List[int] = []
        for i in range(self.v):
            if in_degree[i] == 0:
                queue.append(i)
        result = []
        while queue:
            i = queue.pop(0)
            print("->", i, end=' ')
            result.append(i)
            for j in self.adj[i]:
                in_degree[j] -= 1
                if in_degree[j] == 0:
                    queue.append(j)
        return result

    def topo_sort_by_dfs(self):
        """
        深度优先
        :return:
        """
        # 构造逆领接表
        inverse_adj = [[] for i in range(self.v)]
        for i in range(self.v):
            for j in self.adj[i]:
                inverse_adj[j].append(i)
        visited = [False for i in range(self.v)]
        for i in range(self.v):
            if not visited[i]:
                visited[i] = True
                self.dfs(i, inverse_adj, visited)

    def dfs(self, vertex: int, inverse_adj: List[List[int]], visited: List[bool]):
        for i in inverse_adj[vertex]:
            if visited[i]:
                continue
            visited[i] = True
            self.dfs(i, inverse_adj, visited)
        print("->", vertex, end=' ')


if __name__ == '__main__':
    g = Graph(8)
    # 0,1,2,4,3,5,7,6
    # 5,6,7,0,4,1,3,2
    g.add_edge(0, 1)
    g.add_edge(1, 3)
    g.add_edge(1, 2)
    g.add_edge(0, 3)
    g.add_edge(4, 3)
    g.add_edge(5, 6)
    g.add_edge(5, 7)

    print(g.topo_sort_by_kahn())

    g.topo_sort_by_dfs()
