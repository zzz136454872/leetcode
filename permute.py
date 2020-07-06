from typing import *

def get_next(a):
    i=len(a)-1
    while i>0 and a[i]<a[i-1]:
        i-=1
    if i==0:
        return a
    start=i
    end=len(a)-1
    while start<end:
        tmp=a[start]
        a[start]=a[end]
        a[end]=tmp
        start+=1
        end-=1
    start=i
    i-=1
    while a[start]<a[i]:
        start+=1
    tmp=a[start]
    a[start]=a[i]
    a[i]=tmp
    return a

def fact(a):
    out=1
    while a>1:
        out=out*a
        a-=1
    return out

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return []
        nums.sort()
        f=fact(len(nums))
        out=[]
        for i in range(f):
            out.append(nums.copy())
            nums=get_next(nums)
        return out

sl=Solution()
nums=[1,2,3]
print(sl.permute(nums))

