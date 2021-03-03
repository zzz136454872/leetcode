from typing import *

class Solution:
    def countBits(self, num: int) -> List[int]:
        out=[0,1]
        while len(out)<=num:
            out.extend([i+1 for i in out])
        return out[:num+1]

sl=Solution()
print(sl.countBits(5))
