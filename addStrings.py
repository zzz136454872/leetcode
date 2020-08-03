from typing import *

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1=list(num1)[::-1]
        num2=list(num2)[::-1]
        i=0
        carry=0
        out=[]
        while i<len(num1) or i<len(num2) or carry!=0:
            tmp=carry
            if i<len(num1):
                tmp+=int(num1[i])
            if i<len(num2):
                tmp+=int(num2[i])
            if tmp>9:
                carry=1
                tmp-=10
            else:
                carry=0
            out.append(str(tmp))
            i+=1
        return ''.join(out[::-1])

num1='1234'
num2='9999'
sl=Solution()
print(sl.addStrings(num1,num2))

