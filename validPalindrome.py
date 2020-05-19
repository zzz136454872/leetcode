from typing import *

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s)==0:
            return True
        i=0
        j=len(s)-1
        while i < j-1 and s[i]==s[j]:
            i+=1
            j-=1
        if i >= j-1:
            return True
        old_i=i
        old_j=j
        i+=1
        while i<j and s[i] == s[j]:
            i+=1
            j-=1
        if i>=j:
            return True
        i=old_i
        j=old_j
        j-=1
        while i<j and s[i] == s[j]:
            i+=1
            j-=1
        if i>=j:
            return True
        else:
            return False
sl=Solution()
inp="deeee"
print(sl.validPalindrome(inp))

