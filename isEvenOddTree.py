from collections import deque
from typing import Optional

from pytree import TreeNode


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        level = -1

        while len(queue) > 0:
            queue2 = deque()
            level += 1

            if level % 2 != 0:
                prev = 12345678

                while len(queue) > 0:
                    tmp = queue.popleft()

                    if tmp is None:
                        continue

                    if tmp.val % 2 != 0:
                        return False

                    if tmp.val >= prev:
                        return False
                    prev = tmp.val

                    if tmp.left is not None:
                        queue2.append(tmp.left)

                    if tmp.right is not None:
                        queue2.append(tmp.right)
            else:
                prev = 0

                while len(queue) > 0:
                    tmp = queue.popleft()

                    if tmp is None:
                        continue

                    if tmp.val % 2 == 0:
                        return False

                    if tmp.val <= prev:
                        return False
                    prev = tmp.val

                    if tmp.left is not None:
                        queue2.append(tmp.left)

                    if tmp.right is not None:
                        queue2.append(tmp.right)
            queue = queue2

        return True

root = '[1,10,4,3,null,7,9,12,8,6,null,null,2]'
root = '[5,4,2,3,3,7]'
root = '[5,9,1,3,5,7]'
root = '[1]'
root = '[11,8,6,1,3,9,11,30,20,18,16,12,10,4,2,17]'

print(Solution().isEvenOddTree(TreeNode.fromStrList(root)))
