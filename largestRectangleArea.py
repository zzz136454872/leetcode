from typing import *

class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        heights.insert(0,0)
        stack=[]
        out=0
        #print(heights)
        for i in range(len(heights)):
            while len(stack)>0 and heights[stack[-1]]>heights[i]:
                #print(i,stack,out)
                mid=stack.pop()
                start=stack[-1]+1
                end=i-1
                width=end-start+1
                out=max(out,width*heights[mid])
            stack.append(i)
        return out

inp=[2,1,5,6,2,3]
sl=Solution()
print(sl.largestRectangleArea(inp))
            
