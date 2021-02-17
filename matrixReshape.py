from typing import *

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m=len(nums)
        n=len(nums[0])
        if m*n!=r*c:
            return nums
        tmp=[nums[i][j] for i in range(m) for j in range(n)]
        print(tmp)
        return [[tmp[i*c+j] for j in range(c)] for i in range(r)]

sl=Solution()
nums = [[1,2,3], [4,5,6]]
r = 3
c = 2
print(sl.matrixReshape(nums,r,c))
