from typing import *

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        def find(a,parent):
            if a==parent[a]:
                return a
            parent[a]=find(parent[a],parent)
            return parent[a]

        def union(a,b,parent):
            aa=find(a,parent)
            bb=find(b,parent)
            parent[max(aa,bb)]=min(aa,bb)

        def reduction(parent):
            for i in range(len(parent)):
                find(i,parent)

        edge_group=[[] for i in range(3)]
        for edge in edges:
            edge_group[edge[0]-1].append(edge[1:])

        out=0
        parent0=[i for i in range(n)]
        for edge in edge_group[2]:
            a=find(edge[0]-1,parent0)
            b=find(edge[1]-1,parent0)
            if a!=b:
                union(a,b,parent0)
            else:
                out+=1

        parent1=parent0.copy()
        for edge in edge_group[0]:
            a=find(edge[0]-1,parent0)
            b=find(edge[1]-1,parent0)
            if a!=b:
                union(a,b,parent0)
            else:
                out+=1

        for edge in edge_group[1]:
            a=find(edge[0]-1,parent1)
            b=find(edge[1]-1,parent1)
            if a!=b:
                union(a,b,parent1)
            else:
                out+=1
        
        reduction(parent1)
        reduction(parent0)
        if parent1.count(0)!=n:
            return -1
        return out

n = 4
edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
edges = [[3,2,3],[1,1,2],[2,3,4]]
sl=Solution()
print(sl.maxNumEdgesToRemove(n,edges))
