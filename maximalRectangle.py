from typing import *

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix)==0 or len(matrix[0])==0:
            return 0
        log=[int(num) for num in matrix[0]]
        maxArea=self.largestRectangleArea(log)
        for i in range(1,len(matrix)):
            log=[log[j]+1 if matrix[i][j]=='1' else 0 for j in range(len(matrix[i]))]
            maxArea=max(maxArea,self.largestRectangleArea(log))
        return maxArea
            
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights=[0]+heights+[0]
        stack=[]
        out=0
        for i in range(len(heights)):
            while len(stack)>0 and heights[stack[-1]]>heights[i]:
                mid=stack.pop()
                start=stack[-1]+1
                end=i-1
                width=end-start+1
                out=max(out,width*heights[mid])
            stack.append(i)
        return out

sl=Solution()
inp=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(sl.maximalRectangle(inp))

