class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        mod=1000000007
        log=[[[-1 for kk in range(k+1)] for j in range(m+1)] 
                for i in range(n+1)]
        for i in range(n+1):
            for j in range(m+1):
                log[i][j][0]=0
        for i in range(n+1):
            for kk in range(k+1):
                log[i][0][kk]=0
        for j in range(m+1):
            for kk in range(k+1):
                log[0][j][kk]=0
        # print(log)
        for j in range(1,m+1):
            log[1][j][1]=1
        # print(log[1][0][1])
        # print(log)
        for i in range(1,n+1):
            for j in range(1,m+1):
                for kk in range(1,k+1):
                    if i==1 and kk==1:
                        continue
                    tmp=0
                    for l in range(j):
                        tmp+=log[i-1][l][kk-1]
                    log[i][j][kk]=(j*log[i-1][j][kk]+tmp)%mod
                    # print(i,j,kk,tmp,log[i][j][kk])
        # print(log)
        out=0
        for j in range(m+1):
            out+=log[n][j][k]
        return out%mod

sl=Solution()
n = 5
m = 2
k = 3
print(sl.numOfArrays(n,m,k))
