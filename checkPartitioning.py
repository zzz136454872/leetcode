from typing import *

class Solution:
    def checkPartitioning(self, s: str) -> bool:
        log1=[False for i in range(len(s))]
        log2=[False for j in range(len(s))]
        checked1=[False for i in range(len(s))]
        checked2=[False for i in range(len(s))]

        def check(start,end):
            while start<end:
                if s[start]!=s[end]:
                    return False
                start+=1
                end-=1
            return True

        for i in range(1,len(s)-1):
            l=i
            r=i
            while l>=1 and r<len(s)-1 and s[l]==s[r]:
                if not checked1[l-1]:
                    checked1[l-1]=True
                    if check(0,l-1):
                        log1[l-1]=True
                if not checked2[r+1]:
                    checked2[r+1]=True
                    if check(r+1,len(s)-1):
                        log2[r+1]=True
                if log1[l-1] and log2[r+1]:
                    return True
                l-=1
                r+=1
            l=i
            r=i+1
            while l>=1 and r<len(s)-1 and s[l]==s[r]:
                if not checked1[l-1]:
                    checked1[l-1]=True
                    if check(0,l-1):
                        log1[l-1]=True
                if not checked2[r+1]:
                    checked2[r+1]=True
                    if check(r+1,len(s)-1):
                        log2[r+1]=True
                if log1[l-1] and log2[r+1]:
                    return True
                l-=1
                r+=1

        return False

sl=Solution()
s = "aaaa"
print(sl.checkPartitioning(s))
                    
                   
            
