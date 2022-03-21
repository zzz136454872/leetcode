from typing import Optional

from pytree import TreeNode


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        mem = set()

        def travel(root):
            if root is None:
                return False

            if k - root.val in mem:
                return True
            mem.add(root.val)

            if travel(root.left):
                return True

            if travel(root.right):
                return True

            return False

        return travel(root)
