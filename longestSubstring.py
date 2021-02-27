from typing import *

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        oa=ord('a')
        def ls(s):
            if len(s)==0:
                return 0
            log=[0 for i in range(26)]
            for l in s:
                log[ord(l)-oa]+=1
            cut=-1
            for i in range(26):
                if log[i]>0 and log[i]<k:
                    cut=i
                    break
            if cut==-1:
                return len(s)
            cl=chr(cut+oa)
            return max([ls(ss) for ss in s.split(cl)])
        return ls(s)

sl=Solution()
s = "weitong"
k = 2
print(sl.longestSubstring(s,k))

