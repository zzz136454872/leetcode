

class Solution:
    
    def superEggDrop(self, K: int, N: int) -> int:
        self.log=[[-1 for j in range(N+1)] for i in range(K+1)]
        return self.count(K,N)
        
    def count(self,k,n):
        if n==0:
            return 0
        if k==1:
            return n
        out=self.log[k][n]
        if out!=-1:
            return out
        out=10000000
        for i in range(1,n+1):
            out=min(out,max(self.count(k-1,i-1),self.count(k,n-i))+1)
        self.log[k][n]=out
        return out

sl=Solution()
print(sl.superEggDrop(4,2000))

