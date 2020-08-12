
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        tmp=1
        while tmp<n:
            tmp=tmp*2
        if tmp==n:
            return True
        return False
            

sl=Solution()
inp=16
print(sl.isPowerOfTwo(inp))
