from typing import Optional

from pytree import TreeNode


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        maxLevel = 0
        valSum = 0

        def dfs(root, level):
            nonlocal maxLevel, valSum

            if root is None:
                return

            if level > maxLevel:
                maxLevel = level
                valSum = root.val
            elif level == maxLevel:
                valSum += root.val

            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 1)

        return valSum


