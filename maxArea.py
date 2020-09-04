from typing import *

class Solution:
    def maxArea(self, height: List[int]) -> int:

        left=0
        right=len(height)-1
        out=min(height[left],height[right])*(right-left)
        while left<right:
            if height[left]<height[right]:
                old=height[left]
                left+=1
                while left<len(height) and old>=height[left]:
                    left+=1
                out=max(out,min(height[left],height[right])*(right-left))
            else:
                old=height[right]
                right-=1
                while right>=0 and old>=height[right]:
                    right-=1
                out=max(out,min(height[left],height[right])*(right-left))
        return out

inp=[1,8,6,2,5,4,8,3,7]
sl=Solution()
print(sl.maxArea(inp))

