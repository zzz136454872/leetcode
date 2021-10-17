from typing import Optional

from pytree import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i = 1

        def travel(root):
            if not root:
                return -1
            # print(root.val)
            tmp = travel(root.left)

            if tmp != -1:
                return tmp
            nonlocal i

            if i == k:
                return root.val
            i += 1

            return travel(root.right)

        return travel(root)


root = '[3,1,4,null,2]'
k = 1
root = '[5,3,6,2,4,null,null,1]'
k = 3

root = TreeNode.fromStrList(root)
out = Solution().kthSmallest(root, k)
print(out)
