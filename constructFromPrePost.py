from typing import List

from pytree import TreeNode


class Solution:
    def constructFromPrePost(self, preorder: List[int],
                             postorder: List[int]) -> TreeNode:
        def buildSub(l1, r1, l2, r2):

            # print(l1, r1, l2, r2)

            if l1 > r1:
                return None
            root = TreeNode(preorder[l1])

            if l1 == r1:
                return root
            nr = preorder[l1 + 1]
            i = l2

            while postorder[i] != nr:
                i += 1
            root.left = buildSub(l1 + 1, l1 + 1 + (i - l2), l2, i)
            root.right = buildSub(l1 + 1 + (i - l2) + 1, r1, i + 1, r2 - 1)

            return root

        return buildSub(0, len(preorder) - 1, 0, len(postorder) - 1)


pre = [1, 2, 4, 5, 3, 6, 7]
post = [4, 5, 2, 6, 7, 3, 1]
root = Solution().constructFromPrePost(pre, post)
root.travel(order='pre')
root.travel(order='post')
