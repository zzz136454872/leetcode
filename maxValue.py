from typing import *

class Solution1:
    def maxValue(self, grid: List[List[int]]) -> int:
        log=[[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        for i in range(len(grid)):
            log[i][0]=grid[i][0] +(log[i-1][0] if i>0 else 0) 
        for j in range(len(grid[0])):
            log[0][j]=grid[0][j] +(log[0][j-1] if j>0 else 0)
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                log[i][j]=max(log[i-1][j],log[i][j-1])+grid[i][j]
        print(grid)
        print(log)
        return log[-1][-1]

# 有界数组中指定下标处的最大值
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def count(v):
            out=v
            left_len=min(v,index+1)
            left_height=max(1,v-index)
            left_area=(left_height+v)*left_len//2
            # print('left',left_area)
            right_len=max(0,min(v-1,n-index-1))
            right_height=max(1,v-(n-index-1))
            right_area=(right_height+v-1)*right_len//2
            # print('right',right_area)
            return left_area+right_area
        
        # print('total',count(0))
        maxSum-=n
        l=0
        r=10**9+1
        while l<=r:
            mid=(l+r)//2
            if count(mid)<=maxSum:
                l=mid+1
            else:
                r=mid-1
        return l

sl=Solution()
# grid=[[1,2,5],[3,2,1]]
n = 4
index = 0
maxSum = 4
print(sl.maxValue(n,index,maxSum))

