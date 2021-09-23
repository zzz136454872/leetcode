from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        preMax=-1
        for i in range(len(arr)-1,-1,-1):
            arr[i],preMax=preMax,max(preMax,arr[i])
        return arr

arr = [17,18,5,4,6,1]
print(Solution().replaceElements(arr))

