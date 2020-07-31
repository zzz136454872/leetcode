from typing import *

#totally garbage
class Solution:
    def threeEqualParts(self, A: List[int]) -> List[int]:
        n=A.count(1)
        if n%3!=0:
            return [-1,-1]
        if n==0:
            if len(A)>2:
                return [0,2]
            else:
                return [-1,-1]
        count=0
        for i in range(len(A)):
            if A[i]==1:
                count+=1
                if count==n//3*2+1:
                    loc=i
                    break
        strA=''
        for num in A:
            strA+=str(num)
        num3=int(strA[loc:],2)
        loc2=strA.index(strA[loc:])
        loc2=loc2+len(strA[loc:])
        if loc2>=loc:
            return [-1,-1]

        locmid=loc2+strA[loc2:].index(strA[loc:])
        midend=locmid+len(strA[loc:])
        if midend>loc:
            return [-1,-1]
        num1=int(strA[:loc2],2)
        for i in range(midend,loc+1):
            num2=int(strA[loc2:i],2)
            if num1==num2:
                return [loc2-1,i]
        return [-1,-1]

inp=[1,1,0,0,1]
#inp=[1,1,0,1,1]
#inp=[1,0,1,0,1]
#inp=[0,1,0,1,1]
sl=Solution()
print(sl.threeEqualParts(inp))
        
        

