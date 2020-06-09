from typing import *

class Solution:
    def translateNum(self, num: int) -> int:
        num=str(num)
        log=[0 for i in range(len(num)+1)]
        log[0]=1
        log[1]=1
        for i in range(2,len(log)):
            log[i]=log[i-1]
            if 9<int(num[i-2:i])<26:
                log[i]+=log[i-2]
        return log[-1]
            
sl=Solution()
print(sl.translateNum(12258))
            

        


