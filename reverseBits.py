from typing import *

class Solution:
    def reverseBits(self, n: int) -> int:
        out=0
        for i in range(32):
            out=(out<<1)+(n&1)
            n>>=1
        return out

sl=Solution()
inp='00000010100101000001111010011100'
inp=int(inp,2)
out=sl.reverseBits(inp)
print(bin(out))
