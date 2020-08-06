from typing import *

# not finished
class Solution:
    def getK(self, num: str, k: int) -> str:
        n=len(num)-k
        if n==0:
            return '0'
        stack=[]
        def cmp(a,b):
            return int(a)-int(b)
        for i in range(len(num)):
            while len(stack)>0 and cmp(num[i],stack[-1])<0 and i+1-len(stack)<=k:
                stack.pop()
            stack.append(num[i])
        stack=stack[:n]
        while len(stack)>1 and stack[0]=='0':
            stack.pop(0)
        return ''.join(stack)
    
    def merge(a,b):
        out=[]
        i=0
        j=0
        while a<len(a) or b<len(b):
            flag='b'
            if a<len(a):
                flag='a'
                tmp=a[0]
            if b<len(b) and flag='a' and b[0]>a[0]:
                return False
        return out

    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        return 0
