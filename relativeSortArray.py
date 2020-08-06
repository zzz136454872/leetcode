from typing import *

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        log=[1001 for i in range(1001)]
        for i in range(len(arr2)):
            log[arr2[i]]=i
        out=[]
        for num in arr1:
            out.append((log[num],num))
        out.sort()
        return [sub[1] for sub in out]

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
sl=Solution()
print(sl.relativeSortArray(arr1,arr2))
