from typing import *

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle)==0:
            return 0
        log=[triangle[0][0]]
        for i in range(1,len(triangle)):
            log.insert(0,log[0]+triangle[i][0])
            for j  in range(1,len(triangle[i])-1):
                log[j]=min(log[j],log[j+1])+triangle[i][j]
            log[-1]=log[-1]+triangle[i][-1]
        return min(log)

sl=Solution()
inp=[ [2], [3,4], [6,5,7], [4,1,8,3] ] 
print(sl.minimumTotal(inp))



                    

