from typing import List, Optional

from pytree import TreeNode


class Solution:
    def findDuplicateSubtrees(
            self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        seen = set()
        inRes = set()
        res = []

        def toString(root):
            if root is None:
                return '()'
            r = '(' + toString(root.left) + str(root.val) + toString(
                root.right) + ')'
            # print(r)

            if r in seen:
                if r not in inRes:
                    res.append(root)
                    inRes.add(r)
            else:
                seen.add(r)

            return r

        toString(root)

        return res


root = '[1,2,3,4,null,2,4,null,null,4]'
root = '[0,0,0,0,null,null,0,null,null,null,0]'
root = TreeNode.fromStrList(root)
res = Solution().findDuplicateSubtrees(root)

for r in res:
    TreeNode.travel(r)
