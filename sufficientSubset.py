from typing import Optional

from pytree import TreeNode


class Solution:
    def sufficientSubset(self, root: Optional[TreeNode],
                         limit: int) -> Optional[TreeNode]:
        def find(root, top):
            if root is None:
                return None, 0

            nl, kl = find(root.left, top + root.val)
            nr, kr = find(root.right, top + root.val)
            k = 0

            if root.left != None:
                k = kl

            if root.right != None:
                k = kr

            if root.left != None and root.right != None:
                k = max(kl, kr)
            root.left = nl
            root.right = nr

            if root.val + k + top < limit:
                return None, k + root.val

            return root, k + root.val

        return find(root, 0)[0]


root = '[1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14]'
limit = 1
root = '[5,4,8,11,null,17,4,7,1,null,null,5,3]'
limit = 22
# root = '[1,2,-3,-5,null,4,null]'
# limit = -1

root = TreeNode.fromStrList(root)
root = Solution().sufficientSubset(root, limit)
root.travel()
print(root.toStrList())
