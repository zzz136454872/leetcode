from typing import *

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        n=len(adjacentPairs)+1
        log={}
        for a,b in adjacentPairs:
            if a not in log.keys():
                log[a]=[b]
            else:
                log[a].append(b)
            if b not in log.keys():
                log[b]=[a]
            else:
                log[b].append(a)
        
        out=[]
        # print(log)
        for k in log.keys():
            if len(log[k])==1:
                out.append(k)
                prev=k
                break
        visited={prev}
        
        while True:
            n=log[prev]
            prev=n[0] if n[0] not in visited else n[1]
            out.append(prev)
            visited.add(prev)
            # print('out',prev,visited)
            if len(log[prev])==1:
                break
        return out

adjacentPairs = [[2,1],[3,4],[3,2]]
sl=Solution()
print(sl.restoreArray(adjacentPairs))


