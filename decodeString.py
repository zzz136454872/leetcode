from typing import *

class Solution:
    def decodeString(self, s: str) -> str:
        i=0
        while i<len(s):
            if s[i]==']':
                j=i
                while s[j]!='[':
                    j-=1
                sub=s[j+1:i]
                print(sub)
                p=j-1
                times=0
                while p>=0 and s[p].isdigit():
                    p-=1
                p+=1
                times=int(s[p:j])
                sub=times*sub
                s=s[:p]+sub+s[i+1:]
                print(s)
                i=p
            i+=1
        return s

inp='100[leetcode]'
sl=Solution()
print(sl.decodeString(inp))

