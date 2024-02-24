from bisect import bisect_left, bisect_right
from typing import List, Optional

from pytree import TreeNode


class Solution:
    def closestNodes(self, root: Optional[TreeNode],
                     queries: List[int]) -> List[List[int]]:
        t = []
        res = []

        def f(r):
            if r is None:
                return
            f(r.left)
            t.append(r.val)
            f(r.right)

        f(root)

        for q in queries:
            l1 = bisect_left(t, q)
            l2 = bisect_right(t, q)

            if l2 == 0:
                v2 = -1
            else:
                v2 = t[l2 - 1]

            if l1 == len(t):
                v1 = -1
            else:
                v1 = t[l1]

            res.append([v2, v1])

        return res


root = '[6,2,13,1,4,9,15,null,null,null,null,null,null,14]'
queries = [2, 5, 16]
root = TreeNode.fromStrList(root)
print(Solution().closestNodes(root, queries))
