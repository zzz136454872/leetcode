class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        res=[]
        visited=set()
        mod = 10**n

        def dfs(x):
            res.append(str(x))
            for i in range(k):
                nxt=(x*10+i)%mod
                if nxt not in visited:
                    visited.add(nxt)
                    dfs(nxt)
        
        dfs(0)
        print('res',res)
        return '0'*(n-1)+''.join(res)

n = 1
k = 2
print(Solution().crackSafe(n,k))
       
                    
                
        
