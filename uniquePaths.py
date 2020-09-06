class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a=m+n-2
        b=1
        out=1
        n=min(m,n)-1
        for i in range(n):
            out=out*a//b
            a-=1
            b+=1
        return out

sl=Solution()
print(sl.uniquePaths(7,3))
            
