from typing import *

class Solution1:
    def rotate(self, matrix: List[List[int]]) -> None:
        import copy
        tmp=copy.deepcopy(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[j][len(matrix[0])-1-i]=tmp[i][j]
                print(i,j,tmp[i][j])

inp=[[1,2,3],
  [4,5,6],
  [7,8,9]
]

# 旋转数组
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        if k==0:
            return
        def rev(l,r):
            while l<r:
                tmp=nums[l]
                nums[l]=nums[r]
                nums[r]=tmp
                l+=1
                r-=1
        rev(0,n-1)
        rev(0,k-1)
        rev(k,n-1)

sl=Solution()
inp= [-1,-100,3,99] 
k = 2
sl.rotate(inp,k)
print(inp)



