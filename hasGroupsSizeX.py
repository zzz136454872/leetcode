from typing import List

def gcd(a,b):
        if b==0:
            return a
        return gcd(b,a%b)

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck)==0:
            return False
        nums=dict()
        for num in deck:
            if num in nums.keys():
                nums[num]+=1
            else:
                nums[num]=1
        c=list(nums.values())
        m=min(c)
        for i in range(len(c)):
            m=gcd(m,c[i])
            if m < 2:
                return False
        return True
    


inp=[1,1,2,2,2,2]
sl=Solution()
print(sl.hasGroupsSizeX(inp))
