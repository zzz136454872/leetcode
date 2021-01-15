from typing import *

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        total=set()

        def p2n(p):
            return p[0]+p[1]*10000

        def same(n1,n2):
            return n1%10000==n2%10000 or n1//10000==n2//10000

        stones=[p2n(p) for p in stones]
        father=[i for i in range(len(stones))]
        
        def find(a):
            if father[a]==a:
                return a
            tmp=find(father[a])
            father[a]=tmp
            return tmp

        def merge(a,b):
            ra=find(a)
            rb=find(b)
            if ra!=rb:
                father[max(ra,rb)]=min(ra,rb)

        for i in range(len(stones)-1):
            for j in range(len(stones)):
                if same(stones[i],stones[j]):
                    merge(i,j)

        for i in range(len(stones)):
            r=find(i)
            if r not in total:
                total.add(i)
        return len(stones)-len(total)

sl=Solution()
stones=[[0,0],[0,2],[1,1],[2,0],[2,2]]
print(sl.removeStones(stones))
            
