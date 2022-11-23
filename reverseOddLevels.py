from typing import Optional

from pytree import TreeNode


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def rev(p1, p2, level):
            if p1 is None:
                return

            if level == 0:
                p1.val, p2.val = p2.val, p1.val
            rev(p1.left, p2.right, 1 - level)
            rev(p1.right, p2.left, 1 - level)

        rev(root.left, root.right, 0)

        return root


root = '[2,3,5,8,13,21,34]'
root = TreeNode.fromStrList(root)
res = Solution().reverseOddLevels(root)
res.travel()
