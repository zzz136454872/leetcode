from typing import Optional

from pytree import TreeNode


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        maxLevel = 0
        value = -1

        def dfs(root, level):
            if root is None:
                return
            nonlocal maxLevel, value

            if level > maxLevel:
                maxLevel = level
                value = root.val
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 1)

        return value


root = '[2,1,3]'
root = '[1,2,3,4,null,5,6,null,null,7]'
root = TreeNode.fromStrList(root)
print(Solution().findBottomLeftValue(root))
