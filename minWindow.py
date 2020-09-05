from typing import *

# wa 

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount=dict()
        for l in t:
            if l in tCount.keys():
                tCount[l]+=1
            else:
                tCount[l]=1

        n=len(tCount.keys())
        dic={l:0 for l in tCount.keys()}
        count=0
        l=0
        r=0
        minStr='a'*123456

        while r<len(s):
            while count<n:
                if r<len(s):
                    if s[r] in dic.keys():
                        dic[s[r]]+=1
                        if dic[s[r]]==tCount[s[r]]:
                            count+=1
                    r+=1
                else:
                    break
            while count>=n:
                if len(minStr) > r-l:
                    minStr=s[l:r]
                if s[l] in dic.keys():
                    dic[s[l]]-=1
                    if dic[s[l]]<tCount[s[l]]:
                        count-=1
                l+=1
            
        return minStr if len(minStr)<123456 else ''

S = "AAABBAAAB"
T = "AAAAB"
sl=Solution()
print(sl.minWindow(S,T))


        
