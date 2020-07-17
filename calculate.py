from typing import *

class Solution:

    def calculate(self, s: str) -> int:
        l=[]
        add=
        i=0
        while i<len(s):
            if s[i]==' ':
                i+=1
                continue
            if s[i].isdigit():
                num=int(s[i])
                i+=1
                while s[i].isdigit():
                    num=num*10+int(s[i])
                    i+=1
                l.append(num)
            else:
                l.append(s[i])
                i+=1
        return calc_sub(l)


    def calc_sub(l):
        if len(l)==1:
            return l[0]
        num=l[-1]
        if l[-2] == '+':
            return calc_sub(l[:-2])+num
        if l[-2]=='-':
            return calc_sub(l[:-2])-num

                






