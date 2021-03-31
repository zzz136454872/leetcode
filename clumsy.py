from typing import *

class Solution:
    def clumsy(self, N: int) -> int:
        numStack=[N]
        opStack=[]
        now=0

        def calc(num1,num2,op):
            if op=='+':
                return num1+num2
            if op=='-':
                return num1-num2
            if op=='*':
                return num1*num2
            return num1//num2
        priority={'+':1,'-':1,'*':2,'/':2}
        opDict={0:'*',1:'/',2:'+',3:'-'}

        for i in range(N-1,0,-1):
            while len(opStack)>0 and priority[opStack[-1]]>=priority[opDict[now]]:
                num2=numStack.pop()
                num1=numStack.pop()
                op=opStack.pop()
                numStack.append(calc(num1,num2,op))
            numStack.append(i)
            opStack.append(opDict[now])
            now=(now+1)%4

        while len(opStack)>0:
            num2=numStack.pop()
            num1=numStack.pop()
            op=opStack.pop()
            numStack.append(calc(num1,num2,op))
        return numStack[0]

sl=Solution()
n=10
print(sl.clumsy(n))

        

        
