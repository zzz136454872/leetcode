

def next1(num):
    out=0
    while num>0:
        out+=(num%10)**2
        num=num//10
    return out

class Solution:
    def isHappy(self, n: int) -> bool:
        log=[]
        while True:
            if n==1:
                return True
            n=next1(n)
            if n in log:
                return False
            log.append(n)


inp=19
sl=Solution()
print(sl.isHappy(inp))
            
