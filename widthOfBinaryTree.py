from collections import deque
from typing import Optional

from pytree import TreeNode


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        tmp = deque([(root, 0)])
        maxWidth = 1

        while len(tmp) > 0:
            ntmp = deque()
            idxs = []

            while len(tmp) > 0:
                now, idx = tmp.popleft()

                if now.left is not None:
                    ntmp.append((now.left, idx << 1))
                    idxs.append(idx << 1)

                if now.right is not None:
                    ntmp.append((now.right, (idx << 1) + 1))
                    idxs.append((idx << 1) + 1)

            if len(idxs) > 0:
                maxWidth = max(maxWidth, idxs[-1] - idxs[0] + 1)
            tmp = ntmp

        return maxWidth


root = '[1,3,2,5,3,null,9]'
root = '[1,3,2,5,null,null,9,6,null,7]'
root = '[1,3,2,5]'
root = TreeNode.fromStrList(root)
print(Solution().widthOfBinaryTree(root))
