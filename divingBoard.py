from typing import *

class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k==0:
            return []
        if longer>shorter:
            return [i*longer+(k-i)*shorter for i in range(k+1)]
        else:
            return [k*shorter]
