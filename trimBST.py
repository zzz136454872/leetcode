from typing import Optional

from pytree import TreeNode


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int,
                high: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.val < low:
            return self.trimBST(root.right, low, high)

        if root.val > high:
            return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        return root


root = '[1,0,2]'
low = 1
high = 2

root = '[3,0,4,null,2,null,null,1]'
low = 1
high = 3

root = TreeNode.fromStrList(root)
root = Solution().trimBST(root, low, high)
TreeNode.travel(root)
