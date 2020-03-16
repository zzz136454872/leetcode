import typing
class Solution:
    def compressString(self, S: str) -> str:
        if len(S)==0:
            return S
        out = ""
        i=0
        j=0
        while True:
            out+=S[i]
            j=0
            while i+j<len(S) and S[i]==S[i+j]:
                j+=1
            out+=str(j)
            i+=j
            if i==len(S):
                break
        if len(out) < len(S):
            return out
        return S
inp="aabcccccaaa"
sl=Solution()
print(sl.compressString(inp))
            
