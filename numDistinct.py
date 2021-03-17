
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        log=[[-1]*(len(t)+1) for i in range(len(s)+1)]
        for i in range(len(t)):
            log[len(s)][i]=0
        for i in range(len(s)+1):
            log[i][len(t)]=1

        print(log[len(s)][len(t)])

        def counter(a,b):
            if log[a][b]!=-1:
                return log[a][b]
            if s[a]==t[b]:
                log[a][b]+=counter(a+1,b+1)
            log[a][b]+=counter(a+1,b)+1
            # print(a,b)
            # print(log[a][b])
            return log[a][b]
        
        return counter(0,0)

sl=Solution()
s = "babgbag"
t = "bag"
print(sl.numDistinct(s,t))
        
