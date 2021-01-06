from typing import *

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        start=0
        end=0
        out=[]
        while end<len(s):
            if s[end]!=s[start]:
                if end-start>=3:
                    out.append([start,end-1])
                start=end
            end+=1
        if end-start>=3:
            out.append([start,end-1])
        return out

inp="abc"
sl=Solution()
print(sl.largeGroupPositions(inp))
                
