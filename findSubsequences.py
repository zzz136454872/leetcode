from typing import *

#tle

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def chk(l):
            if len(l)<2:
                return False
            for i in range(len(l)-1):
                if l[i]>l[i+1]:
                    return False
            return True
        out=[]
        for i in range(2,2**len(nums)):
            tmp=bin(i)[2:]
            tmp=(len(nums)-len(tmp))*'0'+tmp
            tmp=list(map(lambda x:x[0],filter(lambda i:int(i[1]),zip(nums,list(tmp)))))
            if chk(tmp):
                out.append(tmp)
        i=0
        while i<len(out)-1:
            j=i+1
            while j<len(out):
                if out[i]==out[j]:
                    del out[j]
                else:
                    j+=1
            i+=1
        return out

sl=Solution()
nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print(sl.findSubsequences(nums))
            
