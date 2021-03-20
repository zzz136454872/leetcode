from typing import *

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for t in tokens:
            if t.isdigit() or t[1:]:
                stack.append(int(t))
            else:
                op_num2=stack.pop()
                op_num1=stack.pop()
                if t=='+':
                    res=op_num1+op_num2
                elif t=='-':
                    res=op_num1-op_num2
                elif t=='*':
                    res=op_num1*op_num2
                elif t=='/':
                    res=int(op_num1/op_num2)
                stack.append(res)
            print(stack)
        return stack[0]

sl=Solution()
tokens = ["2","1","+","3","*"]
tokens = ["4","13","5","/","+"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(sl.evalRPN(tokens))

