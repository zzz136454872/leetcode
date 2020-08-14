from typing import *

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        log={}
        for answer in answers:
            if answer in log.keys():
                log[answer]+=1
            else:
                log[answer]=1
        out=0
        for answer in log.keys():
            c=log[answer]
            if c%(answer+1)==0:
                out+=c
            else:
                out+=(answer+1)*(c//(answer+1)+1)
        return out

sl=Solution()
answers=[0,0,1,1,1]
print(sl.numRabbits(answers))

            
            

