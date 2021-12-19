from typing import Optional

from pytree import TreeNode


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ''

        if root.right is not None:
            r = '(' + self.tree2str(root.right) + ')'

            if root.left is not None:
                l = '(' + self.tree2str(root.left) + ')'
            else:
                l = '()'

            return str(root.val) + l + r

        if root.left is not None:
            return str(root.val) + '(' + self.tree2str(root.left) + ')'

        return str(root.val)


st = '[1,2,3,4]'
st = '[1,2,3,null,4]'
root = TreeNode.fromStrList(st)

print(Solution().tree2str(root))
