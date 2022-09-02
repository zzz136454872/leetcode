from typing import Optional
from pytree import TreeNode

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def sub(r):
            res=[1,1]
            if r.left is not None:
                tmp1=sub(r.left)
                if r.left.val==r.val:
                    res[0]=max(tmp1[1]+1,tmp1[0])
                    res[1]=1+tmp1[1]
                else:
                    res[0]=tmp1[0]
            if r.right is not None:
                tmp2=sub(r.right)
                if r.right.val==r.val:
                    res[0]=max(res[0],tmp2[1]+1,tmp2[0])
                    res[1]=max(res[1],tmp2[1]+1)
                else:
                    res[0]=max(tmp2[0],res[0])

            if r.left is not None and r.right is not None:
                if r.left.val==r.val and r.right.val==r.val:
                    res[0]=max(res[0],tmp1[1]+tmp2[1]+1)
            return res

        return sub(root)[0]-1

root = '[5,4,5,1,1,5]'
root = '[1,2]'
root = TreeNode.fromStrList(root)
print(Solution().longestUnivaluePath(root))
