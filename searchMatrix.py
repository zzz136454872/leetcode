from typing import *

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        y=len(matrix)
        x=len(matrix[0])
        def idx2cord(idx):
            return (idx//x,idx%x)
        
        left=0
        right=x*y-1
        while left<=right:
            mid=(left+right)//2
            cord=idx2cord(mid)
            if matrix[cord[0]][cord[1]]<target:
                left=mid+1
            elif matrix[cord[0]][cord[1]]>target:
                right=mid-1
            else:
                return True
        return False

sl=Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 61
print(sl.searchMatrix(matrix,target))
        
            
