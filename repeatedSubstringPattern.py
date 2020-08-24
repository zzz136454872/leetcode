
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s+s).find(s,1)!=len(s)

s='aba'
sl=Solution()
print(sl.repeatedSubstringPattern(s))
