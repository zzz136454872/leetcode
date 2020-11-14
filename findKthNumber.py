
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count(a):
            out=0
            for i in range(1,n+1):
                out+=min(a//i,m)
                if a<i:
                    break;
            return out

        l=1
        r=m*n
        while l<=r:
            mid=(l+r)//2
            tmp=count(mid)
            if tmp<k:
                l=mid+1
            else:
                r=mid-1
            print(l,r)
        return l
                
sl=Solution()
m = 2
n = 3
k = 6
print(sl.findKthNumber(m,n,k))
