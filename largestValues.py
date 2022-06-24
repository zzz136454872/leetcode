from typing import List, Optional

from pytree import TreeNode


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [(root, 0)]

        while len(stack) > 0:
            now = stack.pop()

            if now[0] is None:
                continue

            if now[1] >= len(res):
                res.append(now[0].val)
            else:
                res[now[1]] = max(res[now[1]], now[0].val)
            stack.append((now[0].left, now[1] + 1))
            stack.append((now[0].right, now[1] + 1))

        return res


root = '[1,3,2,5,3,null,9]'
root = '[1,2,3]'
root = TreeNode.fromStrList(root)
print(Solution().largestValues(root))
