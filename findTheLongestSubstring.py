class Solution:
    
    def findTheLongestSubstring(self, s: str) -> int:
        table={'a':1,'e':2,'i':4,'o':8,'u':16}
        
        now=0
        max_len=0
        before = {0:-1}
        for i in range(len(s)):
            now = now if s[i] not in table.keys() else now^table[s[i]]
            if now not in before.keys():
                before[now]=i
            max_len=max(max_len,i-before[now])
            print(before)
        return max_len

s = "leetcodeisgreat"
sl=Solution()
print(sl.findTheLongestSubstring(s))
            


