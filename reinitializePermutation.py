from typing import *

class Solution:
    def reinitializePermutation(self, n: int) -> int:
        def check(lis):
            for i in range(n):
                if lis[i]!=i:
                    return False
            return True

        perm=[i for i in range(n)]
        time=0
        while True:
            time+=1
            arr=[perm[i//2] if i%2==0 else perm[n//2+(i-1)//2]
                    for i in range(n)]
            if check(arr):
                return time
            perm=arr


sl=Solution()
n=100
print(sl.reinitializePermutation(n))
