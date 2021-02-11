from typing import *
from heapq import heapify, heappush, heappop

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort(reverse=True)
        nums=nums[:k]
        self.heap=nums
        self.k=k
        heapify(self.heap)
        
    def pop_min(self):
        out=self.heap[0]
        tmp=self.heap.pop(-1)
        if len(self.heap)>0:
            self.heap[0]=tmp
            self.adjust(0)
        return out

    def add(self, val: int) -> int:
        if len(self.heap)==self.k and val>self.heap[0]:
            heappop(self.heap)
        if len(self.heap)<self.k:
            heappush(self.heap,val)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
kthLargest = KthLargest(1, []);
print(kthLargest.add(-3))  # return 4
print(kthLargest.add(5))  # return 5
print(kthLargest.add(10)) # return 5
print(kthLargest.add(9))  # return 8
print(kthLargest.add(4))  # return 8

