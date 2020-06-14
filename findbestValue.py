
from typing import *

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        #print(arr)
        front_sum=[0 for i in range(len(arr)+1)]
        tmp=0
        for i in range(1,len(arr)+1):
            tmp+=arr[i-1]
            front_sum[i]=tmp
        #print(front_sum)
        left=0
        right=len(arr)-1
        while left<=right:
            mid = (left+right)//2
            test=front_sum[mid]+arr[mid]*(len(arr)-mid)
            if test<target:
                left=mid+1
            elif test>target:
                right=mid-1
            else:
                return arr[mid]
        miss=target-front_sum[left]
        #print(miss)
        #print(left)
        if left==len(arr):
            return arr[-1]
        return round(miss/(len(arr)-left)-0.000001)
sl=Solution()
inp=[60864,25176,27249,21296,20204]
inp=[4,9,3]
target =10
print(sl.findBestValue(inp,target))
        
