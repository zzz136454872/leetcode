from typing import List

from pytree import TreeNode


class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        def genTree(c):
            if c % 2 == 0:
                return []

            if c == 1:
                return [TreeNode()]
            out = []

            for i in range(1, c - 1, 2):
                left = genTree(i)

                for lt in left:
                    right = genTree(c - 1 - i)

                    for rt in right:
                        out.append(TreeNode(0, lt, rt))

            return out

        return genTree(n)


n = 19
print(Solution().allPossibleFBT(n))
