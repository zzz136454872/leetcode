from typing import *

def ysf(n,m):
    if n==1:
        return 0
    else:
        return (ysf(n-1,m)+m)%n

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        return ysf(n,m)
    
    
