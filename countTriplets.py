from typing import *

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        out=0
        n=len(arr)
        for i in range(n-1):
            tmp=arr[i]
            for j in range(i+1,n):
                tmp^=arr[j]
                if tmp==0:
                    out+=j-i
        return out

sl=Solution()
arr = [7,11,12,9,5,2,7,17,22]
print(sl.countTriplets(arr))

                
