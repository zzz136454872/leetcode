from typing import Optional

from pytree import TreeNode


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if root.left is None and root.right is None and root.val == 0:
            return None

        return root


root = '[1,null,0,0,1]'
root = '[1,0,1,0,0,0,1]'
root = '[1,1,0,1,1,0,1,0]'
root = TreeNode.fromStrList(root)
res = Solution().pruneTree(root)
res.travel()
