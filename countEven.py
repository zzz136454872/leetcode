class Solution:
    def countEven(self, num: int) -> int:
        out=0
        for i in range(2,num+1):
            tmp=0
            while i > 0:
                tmp+=(i%10)
                i//=10
            if tmp%2==0:
                out+=1
        return out

num = 4
# num = 30
print(Solution().countEven(num))
