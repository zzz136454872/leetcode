class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        if n<3:
            return 1
        mem=[1 for i in range(n+1)]
        mem[0]=0
        for i in range(3,n+1):
            mem[i]=mem[i-1]+mem[i-2]+mem[i-3]
        return mem[n]
sl=Solution()
n = 4
n = 25
print(sl.tribonacci(n))
