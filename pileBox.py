from typing import *

class Solution:
    def pileBox(self, box: List[List[int]]) -> int:
        box.sort()
        log=[0 for i in range(len(box))]
        for i in range(len(box)):
            tmp=0
            for j in range(i-1,-1,-1):
                if box[i][1]>box[j][1] and box[i][2]>box[j][2] and box[i][0] > box[j][0]:
                    tmp=max(tmp,log[j])
            log[i]=tmp+box[i][2]

        return max(log)

box = [[1, 1, 1], [2, 3, 4], [2, 6, 7], [3, 4, 5]]
sl=Solution()
print(sl.pileBox(box))
                    
