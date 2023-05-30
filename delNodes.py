from typing import List, Optional

from pytree import TreeNode


class Solution:
    def delNodes(self, root: Optional[TreeNode],
                 to_delete: List[int]) -> List[TreeNode]:
        res = []
        to_delete = set(to_delete)

        def travel(v, pin):
            if v is None:
                return

            if v.val in to_delete:
                if v.left is not None:
                    travel(v.left, False)

                if v.right is not None:
                    travel(v.right, False)

                return None
            else:
                if not pin:
                    res.append(v)
                v.left = travel(v.left, True)
                v.right = travel(v.right, True)

                return v

        travel(root, False)

        return res


root = '[1,2,3,4,5,6,7]'
to_delete = [3, 5]
root = '[1,2,4,null,3]'
to_delete = [3]
root = '[1,2,null,4,3]'
to_delete = [2, 3]
root = TreeNode.fromStrList(root)
res = Solution().delNodes(root, to_delete)
print([x.toStrList() for x in res])
