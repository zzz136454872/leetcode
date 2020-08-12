from typing import *
import math

class Solution:
    def racecar(self, target: int) -> int:
        self.log={}
        dist=0
        for i in range(15):
            self.log[dist]=i
            dist=2*dist+1
        return self.find(target)

    def find(self,n):
        if n in self.log.keys():
            return self.log[n]
        base=math.ceil(math.log(n+1,2))
        tmp1=2**(base-1)-1
        tmp2=2**base-1
        time=base+1+self.find(tmp2-n)
        for i in range(base-1):
            time=min(time,base+1+i+self.find(n-2**(base-1)+2**i))
        self.log[n]=time
        return time

sl=Solution()
target = 3
target = 5
print(sl.racecar(target))
       
        
            
