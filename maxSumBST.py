from typing import Optional

from pytree import TreeNode


class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        res = 0

        def find(node):
            # (s,right,ma,mi):

            if node is None:
                return (0, True, -123456, 123456)
            tl = find(node.left)
            tr = find(node.right)
            right = tl[1] and tr[1] and tl[2] < node.val and node.val < tr[3]
            s = tl[0] + tr[0] + node.val
            lmax = tr[3]
            ma = max(tl[2], tr[2], node.val)
            mi = min(tl[3], tr[3], node.val)
            # print(node.val,s,right,ma,mi)

            if right:
                nonlocal res
                res = max(res, s)

            return (s, right, ma, mi)

        find(root)

        return res


root = '[1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]'
root = '[4,3,null,1,2]'
root = '[-4,-2,-5]'
root = '[2,1,3]'
root = '[5,4,8,3,null,6,3]'
root = TreeNode.fromStrList(root)
print(Solution().maxSumBST(root))
