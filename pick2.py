# 398. 随机数索引

from typing import *

class Solution:
    def rand(self):
        self.now=(self.now*183389)%359753
        return self.now

    def __init__(self, nums: List[int]):
        self.now=1
        self.log={}
        for i in range(len(nums)):
            if nums[i] in self.log.keys():
                self.log[nums[i]].append(i)
            else:
                self.log[nums[i]]=[i]

    def pick(self, target: int) -> int:
        tmp=self.log[target]
        return tmp[self.rand()%len(tmp)]

nums=[1,2,3,3,3]
sl=Solution(nums)
for i in range(10):
    print(sl.pick(3))

        

        
