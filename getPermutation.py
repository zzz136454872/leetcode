
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        table=list('123456789')
        print(table)
        fact=[1 for a in range(n+1)]
        for i in range(1,n+1):
            fact[i]=fact[i-1]*i
        print(fact)
        out=''
        k-=1
        for i in range(n):
            index=k//fact[n-i-1]
            out+=table[index]
            del table[index]
            k=k%fact[n-i-1]
        return out

n = 4
k = 9
sl=Solution()
print(sl.getPermutation(n,k))

       
