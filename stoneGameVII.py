from typing import List

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        presum=[0]
        for s in stones:
            presum.append(presum[-1]+s)
        mem={}
        def dp(s,e):
            if s==e:
                return 0
            if (s,e) in mem:
                return mem[(s,e)]
            v= max(presum[e+1]-presum[s+1]-dp(s+1,e),presum[e]-presum[s]-dp(s,e-1))
            mem[(s,e)]=v
            return v
        return dp(0,len(stones)-1)

stones = [5,3,1,4,2]
stones = [7,90,5,1,100,10,10,2]
print(Solution().stoneGameVII(stones))

