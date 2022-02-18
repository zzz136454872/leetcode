from typing import List

class Solution1:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        log=[a,b,c]
        log.sort()
        if log[2]>=log[0]+log[1]:
            return log[0]+log[1]
        return sum(log)//2

# 执行乘法运算的最大分数
# WA
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
        for i in range(1,n+1):
            out=max(out,log[i][n+1-i])
        return out

nums = [1,2,3]
multipliers = [3,2,1]
print(Solution().maximumScore(nums,multipliers))

# 好子数组的最大分数
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        left=[nums[k]]
        for i in range(k-1,-1,-1):
            if nums[i]<left[-1]:
                left.append(nums[i])
                
        right=[nums[k]]
        for i in range(k+1,len(nums)):
            if nums[i]<right[-1]:
                right.append(nums[i])

        test_points=list(set(left+right))
        test_points.sort(reverse=True)
        l=k
        r=k
        out=0
        for t in test_points:
            while l>=0 and nums[l]>=t:
                l-=1
            while r<len(nums) and nums[r]>=t:
                r+=1
            out=max(out,t*(r-l-1))
        return out
                
# sl=Solution()
# nums = [1,4,3,7,4,5]
# k = 3
# nums = [5,5,4,5,4,1,1,1]
# k = 0
# print(sl.maximumScore(nums,k))
# 
