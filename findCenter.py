from typing import *

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        log={edges[0][0],edges[0][1]}
        if edges[1][0] in log:
            return edges[1][0]
        return edges[1][1]
        
