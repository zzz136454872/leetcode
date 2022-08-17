from typing import Optional

from pytree import TreeNode


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int,
                  depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newNode = TreeNode(val)
            newNode.left = root

            return newNode

        def addSub(root, level):
            if root is None:
                return

            if level == depth - 1:
                n1 = TreeNode(val)
                n2 = TreeNode(val)
                n1.left = root.left
                n2.right = root.right
                root.left = n1
                root.right = n2
            addSub(root.left, level + 1)
            addSub(root.right, level + 1)

        addSub(root, 1)

        return root
