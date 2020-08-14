from typing import *

class Solution:
    def __init__(self, w: List[int]):
        self.table=[0]
        size=0
        self.now=1
        for weight in w:
            size+=weight
            self.table.append(size)
        self.size=size
        self.length=len(w)
    
    def rand(self):
        self.now=(self.now*359981)%100000007
        return self.now%self.size

    def pickIndex(self) -> int:
        r=self.rand()
        end=self.length
        start=0
        while start<=end:
            mid=(start+end)//2
            if self.table[mid]<=r:
                start=mid+1
            else:
                end=mid-1
        return start-1

sl=Solution([1])
for i in range(10):
    print(sl.pickIndex())

