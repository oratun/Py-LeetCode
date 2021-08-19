"""
自己实现一遍，最小堆
"""
from typing import List


class HeapMin:
    def __init__(self, nums: List[int]):
        self.capacity = len(nums)  # 容量
        self.heap = [0] + nums  # 使用数组保存堆，从下标1开始存储
        self.count = self.capacity  # 记录当前堆中元素的数目
        self.build()

    def build(self):
        """建堆"""
        for i in range(self.count // 2, 0, -1):
            self.heapify(i)

    def heapify(self, idx: int):
        """
        堆化  从上往下
        :param idx: 待堆化元素在数组中的位置
        :return:
        """
        while True:
            cur = idx
            if idx * 2 <= self.count and self.heap[idx] > self.heap[idx * 2] and (
                    idx * 2 + 1 > self.count or self.heap[idx * 2] < self.heap[idx * 2 + 1]):
                cur = idx * 2
            elif idx * 2 + 1 <= self.count and self.heap[idx] > self.heap[idx * 2 + 1]:
                cur = idx * 2 + 1
            else:
                break
            self.heap[idx], self.heap[cur] = self.heap[cur], self.heap[idx]
            idx = cur

    def pop(self):
        """
        弹出元素
        :return:
        """
        if self.count:
            ret = self.heap[1]
            self.count -= 1
            if self.count:
                self.heap[1] = self.heap[self.count + 1]
                self.heapify(1)
            return ret

    def push(self, val: int):
        """
        入堆
        :param val:la
        :return:
        """
        if self.count < self.capacity:
            self.heap.append(val)
            self.count += 1
            self.heapify(self.count)


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    h = HeapMin([-i for i in nums])
    for i in range(len(nums)):
        print(-h.pop())
