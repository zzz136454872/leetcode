from typing import *


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        mem = [[0] * (n + 1) for i in range(m + 1)]
        
        for i in range(len(strs)):
            c0=strs[i].count('0')
            c1=strs[i].count('1')
            mem_old=mem
            mem = [[0] * (n + 1) for i in range(m + 1)]
            for j in range(m+1):
                for k in range(n+1):
                    if j>=c0 and k>=c1:
                        mem[j][k]=max(mem_old[j-c0][k-c1]+1,mem_old[j][k])
                    else:
                        mem[j][k]=mem_old[j][k]
        return mem[-1][-1]

sl=Solution()
strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
strs = ["10", "0", "1"]
m = 1
n = 1
print(sl.findMaxForm(strs,m,n))



