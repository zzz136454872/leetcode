class Solution:
    def countHomogenous(self, s: str) -> int:
        j=0
        i=0
        res=0
        mod=10**9+7
        while i<len(s):
            while j<len(s) and s[j]==s[i]:
                j+=1
            tmp=j-i
            res=(res+(tmp+1)*tmp//2)%mod 
            i=j
        return res

s = "abbcccaa"
s = "xy"
s = "zzzzz"
print(Solution().countHomogenous(s))
                
