

class Solution:
    
    def superEggDrop(self, K: int, N: int) -> int:
        self.log=[[-1 for j in range(N+1)] for i in range(K+1)]
        out=self.count(K,N)
        return out
        
    def count(self,k,n):
        if n==0:
            return 0
        if k==1:
            return n
        out=self.log[k][n]
        if out!=-1:
            return out
        out=10000000
        start=1
        end=n
        while start<=end:
            mid=(start+end)//2
            broke=self.count(k-1,n-mid)
            not_broke=self.count(k,mid-1)
            out=min(out,max(broke,not_broke)+1)
            if broke==not_broke:
                break
            elif broke>not_broke:
                start=mid+1
            else:
                end=mid-1
        self.log[k][n]=out
        return out

sl=Solution()
print(sl.superEggDrop(3,80))

