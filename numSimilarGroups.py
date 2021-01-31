from typing import *

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n=len(strs)
        if n<=1:
            return n
        ln=len(strs[0])
        parent={i:i for i in strs}

        def find(a):
            if a==parent[a]:
                return a
            parent[a]=find(parent[a])
            return parent[a]

        def union(a,b):
            aa=find(a)
            bb=find(b)
            parent[max(aa,bb)]=min(aa,bb)

        def reduction():
            for k in parent.keys():
                find(k)

        def same(a,b):
            diff=0
            for i in range(ln):
                if a[i]!=b[i]:
                    diff+=1
            return diff==2 or diff==0

        for i in range(n-1):
            for j in range(i+1,n):
                pi=find(strs[i])
                pj=find(strs[j])
                if pi!=pj and same(strs[i],strs[j]):
                    union(pi,pj)
        reduction()
        return len(set(parent.values()))

sl=Solution()
strs = ["tars","rats","arts","star"]
print(sl.numSimilarGroups(strs))
            
    
