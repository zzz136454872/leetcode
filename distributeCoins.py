from typing import Optional

from pytree import TreeNode


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = 0

        def find(r):
            if r is None:
                return (0, 0)
            ll = find(r.left)
            rr = find(r.right)
            c = ll[0] + rr[0] + 1
            t = ll[1] + rr[1] + r.val
            nonlocal res
            res += abs(c - t)

            return (c, t)

        find(root)

        return res


root = '[3,0,0]'
root = '[0,3,0]'
root = '[1,0,2]'
root = '[1,0,0,null,3]'
root = TreeNode.fromStrList(root)
print(Solution().distributeCoins(root))
