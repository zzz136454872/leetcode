from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
            sR=ord(s[0])
            sC=int(s[1])
            eR=ord(s[3])
            eC=int(s[4])
            out=[]
            for i in range(sR,eR+1):
                for j in range(sC,eC+1):
                    out.append(chr(i)+str(j))
            return out

s = "K1:L2"
s = "A1:F1"
print(Solution().cellsInRange(s))
                    
