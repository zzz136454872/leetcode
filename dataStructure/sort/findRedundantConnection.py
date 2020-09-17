from typing import *

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent={i+1:i+1 for i in range(n)}
        def find(x):
            if parent[x]==x:
                return x
            return find(parent[x])
        def union(x,y):
            rx=find(x)
            ry=find(y)
            parent[rx]=ry

        for edge in edges:
            if find(edge[0])==find(edge[1]):
                return edge
            union(edge[0],edge[1])

        return [-1,-1] # not going here

sl=Solution()
edges=[[1,2], [2,3], [3,4], [1,4], [1,5]]
print(sl.findRedundantConnection(edges))

