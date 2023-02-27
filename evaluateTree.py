from typing import Optional

from pytree import TreeNode


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return root.val == 1

        if root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(
                root.right)

        return self.evaluateTree(root.left) and self.evaluateTree(root.right)


root = '[2,1,3,null,null,0,1]'
root = '[0]'
root = TreeNode.fromStrList(root)
print(Solution().evaluateTree(root))
