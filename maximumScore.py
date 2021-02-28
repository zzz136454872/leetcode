from typing import *

class Solution1:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        log=[a,b,c]
        log.sort()
        if log[2]>=log[0]+log[1]:
            return log[0]+log[1]
        return sum(log)//2

# 执行乘法运算的最大分数

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n=len(multipliers)
        log=[[0 for i in range(n+1)] for j in range(n+1)]
        for i in range(n):
            for l in range(1,i+2):
                r=i+2-l 
                tmp=max(log[l-1][r]+nums[l-1]*multipliers[i],
                        log[l][r-1]+nums[n-r]*multipliers[i])
                log[l][r]=tmp
                
        out=-123456789
        print(log)
        for i in range(n+1):
            out=max(out,log[i][n-i])
        return out

sl=Solution()
a = 4
b = 4
c = 6
nums = [1,2]
multipliers = [2,1]
# nums = [-5,-3,-3,-2,7,1]
# multipliers = [-10,-5,3,4,6]
print(sl.maximumScore(nums,multipliers))

