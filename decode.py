from typing import *

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n=len(encoded)+1
        all_xor=0
        for i in range(1,n+1):
            all_xor^=i
        sub_xor=0
        for i in range(1,n-1,2):
            sub_xor^=encoded[i]
        start=all_xor^sub_xor
        out=[start]
        for n in encoded:
            out.append(out[-1]^n)
        return out

sl=Solution()
encoded = [3,1]
encoded = [6,5,4,6]
print(sl.decode(encoded))
        



