
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<=1:
            return False
        s=1
        i=2
        while i*i<num:
            if num%i==0:
                s+=i+num//i
            i+=1
        if i*i==num and num%i==0:
            s+=i
        return s==num

sl=Solution()
print(sl.checkPerfectNumber(28))
    
