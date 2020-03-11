class Solution:
    def canThreePartsEqualSum(self, A) -> bool:
        if len(A)==0:
            return False
        s=sum(A)
        if s%3!=0:
            return False
        else:
            s=s//3
        tmp=A[0]
        i=0
        while tmp!=s and i<len(A)-1:
            i+=1
            tmp+=A[i]
        if i==len(A)-1:
            return False
        i+=1
        tmp=A[i]
        while tmp!=s and i<len(A)-1:
            i+=1
            tmp+=A[i]
        if(i==len(A)-1):
            return False
        return True

sl=Solution()
inp=[0,2,1,-6,6,7,9,-1,2,0,1]
print(sl.canThreePartsEqualSum(inp))

        
            
            
        
