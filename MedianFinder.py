from typing import *

class MedianFinder:

    def __init__(self):
        self.log=[]

    def addNum(self, num: int) -> None:
        self.log.append(num)

    def findMedian(self) -> float:
        self.log.sort()
        return (self.log[len(self.log)//2]+self.log[(len(self.log)-1)//2])/2

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3) 
print(obj.findMedian())
