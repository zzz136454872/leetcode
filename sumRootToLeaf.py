from typing import Optional

from pytree import TreeNode


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        value = 0
        res = 0

        def dfs(root, value):
            if not root:
                return
            value = 2 * value + root.val

            if not root.left and not root.right:
                nonlocal res
                res += value

                return
            dfs(root.left, value)
            dfs(root.right, value)

        dfs(root, 0)

        return res
