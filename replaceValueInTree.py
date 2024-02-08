from typing import Optional

from pytree import TreeNode


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pp = {}
        mem = []

        def func1(p, node, level):
            if level >= len(mem):
                mem.append(0)
            mem[level] += node.val
            pp[p] = pp.get(p, 0) + node.val

        def func2(p, node, level):
            node.val = mem[level] - pp[p]

        def dfs(p, node, level, f):
            if node is None:
                return
            f(p, node, level)
            dfs(node, node.left, level + 1, f)
            dfs(node, node.right, level + 1, f)

        dfs(None, root, 0, func1)
        dfs(None, root, 0, func2)

        return root


root = '[5,4,9,1,10,null,7]'
root = '[3,1,2]'
root = TreeNode.fromStrList(root)
res = Solution().replaceValueInTree(root)
TreeNode.travel(res)
