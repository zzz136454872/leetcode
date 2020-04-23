
m=1000000007
def l2(n):
    return (((n+3)//2)*((n+2)//2))%m
class Solution:
    def waysToChange(self, n: int) -> int:
        test=n//5
        # test2=test//2
        # test5=test//5
        # log2=[]

        # for i in range(test+1):
        #     tmp=0
        #     for j in range(i//2+1):
        #         tmp+=(i-2*j+1)%m
        #     log2.append(tmp)

        out=0
        for i in range(test//5+1):
            out=(out+l2(test-5*i))%m
        return out
       

sl=Solution()
print(sl.waysToChange(900750))


                



        
