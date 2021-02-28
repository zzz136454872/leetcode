from typing import *

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes=[int(i) for i in boxes]
        left=[0 for i in boxes]
        right=[0 for i in boxes]
        tmp=0
        
        for i in range(len(boxes)):
            left[i]=tmp
            tmp+=boxes[i]
        tmp=0
        for i in range(len(boxes)-1,-1,-1):
            right[i]=tmp
            tmp+=boxes[i]
        tmp=0
        for i in range(len(boxes)):
            if boxes[i]:
                tmp+=i
        out=[tmp]
        print(left,right)
        for i in range(1,len(boxes)):
            tmp+=left[i]-right[i-1]
            out.append(tmp)
        return out

boxes = "001011"
sl=Solution()
print(sl.minOperations(boxes))
