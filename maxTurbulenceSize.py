from typing import *

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr)<=1:
            return len(arr)
        def sub(loc):
            a= arr[loc]-arr[loc-1]
            if a>0:
                return 1
            if a==0:
                return 0
            return -1
        out=1
        last=-sub(1)
        start=0
        for i in range(1,len(arr)):
            if sub(i)*last<0:
                out=max(out,i-start+1)
                last=-last
            else:
                start=i-1
                last=sub(i)
        return out

sl=Solution()
# arr=[9,4,2,10,7,8,8,1,9]
arr=[1,2,3,4]
print(sl.maxTurbulenceSize(arr))
