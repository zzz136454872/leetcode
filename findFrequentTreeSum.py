from typing import List

from pytree import TreeNode


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        mem = {}

        def travel(root):
            if not root:
                return 0
            tmp = root.val + travel(root.left) + travel(root.right)
            mem[tmp] = mem.get(tmp, 0) + 1

            return tmp

        travel(root)
        mv = max(mem.values())

        return [k for k, v in mem.items() if v == mv]


root = '[5,2,-3]'
root = '[5,2,-5]'
root = TreeNode.fromStrList(root)
print(Solution().findFrequentTreeSum(root))
