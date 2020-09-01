from typing import *

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        table=[0 for i in range(len(arr)+1)]
        for i in range(len(arr)):
            table[i+1]=table[i]^arr[i]
        out=[]
        for pair in queries:
            out.append(table[pair[0]]^table[pair[1]+1])
        return out

arr = [1,3,4,8]
queries = [[0,1],[1,2],[0,3],[3,3]]
sl=Solution()
print(sl.xorQueries(arr,queries))
