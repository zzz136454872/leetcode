from typing import *

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
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

num = "10200"
k = 1
num = "123456789"
k = 3
sl=Solution()
print(sl.removeKdigits(num,k))
    
