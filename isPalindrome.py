from typing import *

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=list(s)
        for i in range(len(s)):
            if not s[i].isdigit() and not s[i].isalpha():
                s[i]=""
                continue
            s[i]=s[i].lower()
        s="".join(s)
        return s==s[::-1]

sl=Solution()
inp="A man, a plan, a canal: Panama"
inp="0P"
print(sl.isPalindrome(inp))
