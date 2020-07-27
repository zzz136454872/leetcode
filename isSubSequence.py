from typing import *

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        if len(s)==0:
            return True
        for letter in t:
            if letter==s[j]:
                j+=1
                if j==len(s):
                    return True
        return False

sl=Solution()
s = "abcf"
t = "ahbgdc"
print(sl.isSubsequence(s,t))
