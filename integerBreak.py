from typing import *

class Solution:
    def integerBreak(self, n: int) -> int:
        log=[-1 for i in range(max(n+1,5))]
        log[0]=0
        log[1]=0
        log[2]=1
        log[3]=2
        log[4]=4
        if n<=4:
            return log[n]
        def get_num(num):
            if num<=4:
                return num
            if log[num]>=0:
                return log[num]
            out=0
            for i in range(2,num//2+1):
                out=max(out,get_num(i)*get_num(num-i))
            log[num]=out
            return out
        return get_num(n)
sl=Solution()
n=10
print(sl.integerBreak(n))

                
            
                
        
    
