from typing import *

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # print('start',s1,s2)
        if len(s1)!=len(s2):
            return False
        if s1==s2:
            return True
        if sorted(s1)!=sorted(s2):
            return False
        n=len(s1)
        # print('out',s1,s2)
        for i in range(1,len(s1)):
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]):
                return True
            if self.isScramble(s1[:i],s2[n-i:]) and self.isScramble(s1[i:],s2[:n-i]):
                return True
        return False

s1="abcdbdac"
s2="bdacabcd"
sl=Solution()
print(sl.isScramble(s1,s2))
