class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K==0:
            return 1.0
        if K+W-1<N:
            return 0.0
        dp=[0 for i in range(N+1)]
        dp[0]=1
        now=0
        for i in range(1,N+1):
            if i <= K:
                now+=dp[i-1]
            if i-W-1>=0:
                now-=dp[i-W-1]
            dp[i]=now/W
            #print(dp)
        return sum(dp[K:])
            
N=21
K=17
W=10
sl=Solution()
print(sl.new21Game(N,K,W))


