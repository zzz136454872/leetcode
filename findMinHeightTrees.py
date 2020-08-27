from typing import *

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes=set([i for i in range(n)])
        while len(nodes)>2:
            counter=dict().fromkeys(nodes,0)
            for edge in edges:
                counter[edge[0]]+=1
                counter[edge[1]]+=1
            for n in nodes:
                if counter[n]==0:
                    nodes.remove(n)
            edges=list(filter(lambda x: x[0] in nodes and x[1] in nodes,edges))
        return list(nodes)

n = 4
edges = [[1, 0], [1, 2], [1, 3]]
sl=Solution()
print(sl.findMinHeightTrees(n,edges))

