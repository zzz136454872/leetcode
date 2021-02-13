from typing import *

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        start=0
        end=0
        for i in range(1,len(arr)):
            if arr[i]<arr[i-1]:
                if start==0:
                    start=i
                end=i

        if start==0:
            return 0
        j=end
        out=min(len(arr)-start,end)
        print(out,start,end)
        for i in range(start):
            while j<len(arr) and arr[i]>arr[j]:
                j+=1
            out=min(out, j-i-1)
        return out

sl=Solution()
arr=[16,10,0,3,22,1,14,7,1,12,15]
# output:10
# wanting: 8
print(sl.findLengthOfShortestSubarray(arr))


