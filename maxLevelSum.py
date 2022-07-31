from typing import Optional

from pytree import TreeNode


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        nxt = [root]
        maxSum = -10**10 - 1
        maxLevel = 0
        level = 0

        while len(nxt) > 0:
            level += 1
            tmp = nxt
            nxt = []
            s = 0

            while len(tmp) > 0:
                now = tmp.pop()

                if now.left is not None:
                    nxt.append(now.left)

                if now.right is not None:
                    nxt.append(now.right)
                s += now.val

            if s > maxSum:
                maxSum = s
                maxLevel = level

        return maxLevel


root = '[1,7,0,7,-8,null,null]'
root = '[989,null,10250,98693,-89388,null,null,null,-32127]'
root = TreeNode.fromStrList(root)
print(Solution().maxLevelSum(root))
