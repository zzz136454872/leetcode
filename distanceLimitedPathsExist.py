from typing import *

class Solution:
    def distanceLimitedPathsExist(self,
            n: int,
            edgeList: List[List[int]],
            queries: List[List[int]]) -> List[bool]:
        queries=[(i,*queries[i]) for i in range(len(queries))]
        queries.sort(key=lambda x:x[3])
        out=[]
        parent=[i for i in range(n)]

        def find(a):
            if a==parent[a]:
                return a
            parent[a]=find(parent[a])
            return parent[a]

        def union(a,b):
            aa=find(a)
            bb=find(b)
            parent[max(aa,bb)]=min(aa,bb)
        
        edgeList.sort(key=lambda x:x[2])
        ec=0
        for q in queries:
            while ec<len(edgeList) and edgeList[ec][2]<q[3]:
                union(edgeList[ec][0],edgeList[ec][1])
                ec+=1
            out.append((q[0],find(q[1])==find(q[2])))
        out.sort()
        return [o[1] for o in out]

sl=Solution()
n = 5
edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]]
queries = [[0,4,14],[1,4,13]]
print(sl.distanceLimitedPathsExist(n,edgeList,queries))
        
