from typing import *

def get_priority(op):
    if op=='+' or op=='-':
        return 0
    if op=='*' or op=='/':
        return 1
    if op=='(':
        return -1
    if op==')':
        return 2

def calc(num1,num2,op):
    if op=='+':
        return num1+num2
    if op=='-':
        return num1-num2
    if op=='*':
        return num1*num2
    if op=='/':
        return num1//num2

class Solution:
    def calculate(self, s: str) -> int:
        s=s.replace(' ','')
        l=[]
        i=0
        while i<len(s):
            if s[i].isdigit():
                num=int(s[i])
                i+=1
                while i<len(s) and s[i].isdigit():
                    num=num*10+int(s[i])
                    i+=1
                l.append(num)
            else:
                if s[i]=='-' and (i==0 or not s[i-1].isdigit()):
                    l.append(0)
                l.append(s[i])
                i+=1
        i=0
        num_stack=[]
        op_stack=[]

        while i<len(l):
            # print(i,num_stack)
            # print(i,op_stack)
            if type(l[i])==int:
                num_stack.append(l[i])
            elif l[i]==')':
                while op_stack[-1]!='(':
                    op=op_stack.pop()
                    num2=num_stack.pop()
                    num1=num_stack.pop()
                    num_stack.append(calc(num1,num2,op))
                op_stack.pop()
            elif l[i]=='(':
                op_stack.append(l[i])
            else:
                while len(op_stack)>0 and\
                        get_priority(op_stack[-1])>=get_priority(l[i]):
                    op=op_stack.pop()
                    num2=num_stack.pop()
                    num1=num_stack.pop()
                    num_stack.append(calc(num1,num2,op))
                op_stack.append(l[i])
            i+=1
        print('out')
        while len(op_stack)>0:
            print(op_stack)
            print(num_stack)
            op=op_stack.pop()
            num2=num_stack.pop()
            num1=num_stack.pop()
            num_stack.append(calc(num1,num2,op))
        print(num_stack)
        return num_stack[0]

s="0-2147483647"
sl=Solution()
print(sl.calculate(s))
