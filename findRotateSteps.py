from typing import *

class Solution:

    def findRotateSteps(self, ring: str, key: str) -> int:

        def l2n(a):
            return ord(a)-ord('a')

        log=[[] for i in range(26)]
        for i in range(len(ring)):
            log[l2n(ring[i])].append(i)
        mem=[{} for j in range(len(key)+1)] 
        mem[0][0]=0
        
        def dist(a,b):
            if a<b:
                a,b=b,a
            return min(a-b,b+len(ring)-a)
        
        for i in range(len(key)):
            for loc_end in log[l2n(key[i])]:
                tmp_min=2000000
                for loc in mem[i].keys():
                    tmp_min=min(tmp_min,mem[i][loc]+dist(loc,loc_end))
                mem[i+1][loc_end]=tmp_min
        return min(mem[-1].values())+len(key)

sl=Solution()
ring="cfcdbgehlm"
key="dcgmhecgfgldbfmlchcldcbdgmlfbccclbfmmcceflggcfcdcffhbbcchdclhghmchcedgcbdbhddlmeelembfbcfememhlggehe"
print(sl.findRotateSteps(ring, key))

