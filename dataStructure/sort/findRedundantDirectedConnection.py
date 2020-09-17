from typing import *

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent={i+1:i+1 for i in range(n)}
        log=-1
        for edge in edges:
            if parent[edge[1]]!=edge[1]:
                log=edge[1]
            parent[edge[1]]=edge[0]

        def find(x,parent1):
            if x==parent1[x]:
                return x;
            else:
                return find(parent1[x],parent1)

        def union(x,y,parent1):
            rx=find(x,parent1)
            ry=find(y,parent1)
            parent1[rx]=ry

        if log==-1: #no node has indegree 2
            parent1={i+1:i+1 for i in range(n)}
            for edge in edges:
                if find(edge[0],parent1)==find(edge[1],parent1):
                    return edge
                union(edge[0],edge[1],parent1);
        else:
            parent1={i+1:i+1 for i in range(n)}
            base=[]
            for edge in edges:
                if edge[1]==log:
                    base.append(edge)
                    continue
                union(edge[0],edge[1],parent1);
            assert(len(base)==2)
            edge=base[0]
            if find(edge[0],parent1)==find(edge[1],parent1):
                return base[0]
            else:
                return base[1]

sl=Solution()
edges=[[1,2], [2,3], [3,4], [4,1], [1,5]]
print(sl.findRedundantDirectedConnection(edges))
         
