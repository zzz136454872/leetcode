from typing import *

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        log={'U':0,'D':0,'L':0,'R':0}
        for m in moves:
            log[m]+=1
        return log['U']==log['D'] and log['L']==log['R']


