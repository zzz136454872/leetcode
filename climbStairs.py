
class Solution:
    def climbStairs(self, n: int) -> int:
        log = [1 for i in range(n)]
        if n==1:
            return 1
        if n==2:
            return 2
        log[0]=1
        log[1]=2
        for i in range(2,n):
            log[i]=log[i-1]+log[i-2]
        return log[-1]
sl=Solution()
print(sl.climbStairs(3))
        
        
