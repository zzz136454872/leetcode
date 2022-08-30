from typing import Optional

from pytree import TreeNode


class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode],
                          val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        if val > root.val:
            nnode = TreeNode(val)
            nnode.left = root

            return nnode
        root.right = self.insertIntoMaxTree(root.right, val)
        return root
