from typing import List
from collections import Counter
from functools import cache
import cProfile 

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        kk=len(nums)//k
        if kk==1:
            return 0
        c=dict(Counter(nums))
        if max(c.values())>k:
            return -1

        @cache
        def gen(d,s,t):
            if t==0:
                return [[]]
            res=[]
            for i in range(s,len(d)-t+1):
                r=gen(d,i+1,t-1)
                for rr in r:
                    rr=rr.copy()
                    rr.append(d[i])
                    res.append(rr)
            return res
        
        big=12345678

        def bt():
            if len(c)==0:
                return 0
            mindiff=big

            ks=list(c.keys())
            fix=min(c.keys())
            ks.remove(fix)
            c[fix]-=1
            if c[fix]==0:
                del c[fix]
            for choose in gen(tuple(ks),0,kk-1):
                diff=max(max(choose),fix)-min(min(choose),fix)
                for num in choose:
                    c[num]-=1
                    if c[num]==0:
                        del c[num]
                diff+=bt()
                mindiff=min(mindiff,diff)
                for num in choose:
                    c[num]=c.get(num,0)+1
            c[fix]=c.get(fix,0)+1
            return mindiff

        return bt()

nums = [1,2,1,4]
k = 2
nums = [6,3,8,1,3,1,2,2,1,2,3,4,5,6,7,8]
k = 4
# nums = [1,2,2,3]
# k = 2
# nums = [5,3,3,6,3,3]
# k = 3
# nums=[7,3,16,15,1,13,1,2,14,5,3,10,6,2,7,15]
# k=8
nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
k=8
cProfile.run('print(Solution().minimumIncompatibility(nums,k))')
            