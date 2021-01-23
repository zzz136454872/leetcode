from typing import *

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        log=[i for i in range(n)]
        def find(a):
            if a==log[a]:
                return a
            log[a]=find(log[a])
            return log[a]

        def union(a,b):
            a=find(a)
            b=find(b)
            if a!=b:
                log[max(a,b)]=min(a,b)
        
        for a,b in connections:
            union(a,b)
        for i in range(n):
            find(i)
        return len(set(log))-1

sl=Solution()
n = 5
connections = [[0,1],[0,2],[3,4],[2,3]]
print(sl.makeConnected(n,connections))
            
            
