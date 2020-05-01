import heapq
from typing import List


class MaxHeap:
    def __init__(self):
        self.data = []

    def top(self):
        return -self.data[0]

    def push(self, val):
        heapq.heappush(self.data, -val)

    def pop(self):
        return -heapq.heappop(self.data)


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        diff = 0
        heap = MaxHeap()

        for s in stones:
            heap.push(s)
        
        while True:
            try:
                one = heap.pop()
            except IndexError:
                return diff
            
            try:
                two = heap.pop()
            except IndexError:
                return one

            diff = one - two
            if diff != 0:
                heap.push(diff)

        return diff
