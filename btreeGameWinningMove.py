from typing import Optional

from pytree import TreeNode


class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int,
                             x: int) -> bool:
        def dfs1(r):
            if r is None:
                return None

            if r.val == x:
                return r
            l = dfs1(r.left)

            if l is not None:
                return l

            return dfs1(r.right)

        p = dfs1(root)

        def dfs2(r):
            if r is None or r == p:
                return 0

            return 1 + dfs2(r.left) + dfs2(r.right)

        c1 = dfs2(root)
        c2 = dfs2(p.left)
        c3 = dfs2(p.right)

        return c1 > n // 2 or c2 > n // 2 or c3 > n // 2


root = '[1,2,3,4,5,6,7,8,9,10,11]'
n = 11
x = 3
root = '[1,2,3]'
n = 3
x = 1
root = TreeNode.fromStrList(root)
print(Solution().btreeGameWinningMove(root, n, x))
