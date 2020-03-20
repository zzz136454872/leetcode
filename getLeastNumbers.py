from typing import *

#class Solution:
#    def getLeastNumbers(self, arr, k: int) -> List[int]:
#        if k==0:
#            return []
#        out=arr[:k]
#        out.sort()
#        print(out)
#        for i in range(k,len(arr)):
#            if arr[i]>=out[-1]:
#                continue
#            j=0
#            while j<k-1 and out[j]<=arr[i]:
#                j+=1
#            out.insert(j,arr[i])
#            out=out[:-1]
#        return out

class Solution:
    def getLeastNumbers(self, arr, k: int) -> List[int]:
        return sorted(arr)[:k]

arr=[3,2,1]
k=2
sl=Solution()
print(sl.getLeastNumbers(arr,k))
                


