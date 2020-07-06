from typing import *

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i=0
        if len(s)==0:
            if len(p.replace('*',''))!=0:
                return False
            return True
        while i<len(p) and i<len(s) and p[i]!='*':
            if self.match(s[i],p[i]):
                i+=1
            else:
                return False
        if i==len(p):
            return True if i==len(s) else False
        p=p[i:]
        s=s[i:]
        i=1
        if len(s)==0:
            if len(p.replace('*',''))!=0:
                return False
            return True
        while i<=len(p) and i<=len(s) and p[-i]!='*':
            if self.match(s[-i],p[-i]):
                i+=1
            else:
                return False
        end=i
        #print(end)
        s=s[:len(s)-end+1]
        p=p[:len(p)-end+1]
        #print(s,p)
        pList=p.split('*')
        while '' in pList:
            pList.remove('')
        print(s,pList)
        for pSub in pList:
            i=0
            #print(s)
            while i<len(pSub):
                if i<len(s):
                    if self.match(s[i],pSub[i]):
                        i+=1
                    else:
                        s=s[1:]
                        i=0
                else:
                    return False
            s=s[len(pSub):]
        return True

    def match(self,a,b):
        if a==b:
            return True
        if b=='?':
            return True
        return False

sl=Solution()
s="mississippi"
p="m??*ss*?i*pi"
#s='c'
#p='*?*'
print(sl.isMatch(s,p))

