from typing import *

def abs(a):
    return a if a>0 else -a

class Solution:
    def cmp(self,x,y):
        tmp=abs(x-self.m)-abs(y-self.m)
        if tmp>0:
            return 1
        if tmp<0:
            return -1
        return x-y

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        if len(arr)<=k:
            return arr
        arr.sort()
        n=len(arr)
        self.m=arr[(n-1)//2]
        print(self.m)
        start=0
        end=n-1
        out=[]
        for i in range(k):
            if self.cmp(arr[start],arr[end])>0:
                out.append(arr[start])
                start+=1
            else:
                out.append(arr[end])
                end-=1
        return out
arr = [-7,22,17,3]
k=2
sl=Solution()
print(sl.getStrongest(arr,k))
