from pytree import TreeNode


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        mem = {}
        mem[None] = 0

        def genDepth(root):
            if root is None:
                return 0
            tmp = max(genDepth(root.left), genDepth(root.right))
            mem[root] = tmp + 1

            return tmp + 1

        genDepth(root)

        def findDeepest(root):
            if mem[root.left] == mem[root.right]:
                return root
            elif mem[root.left] > mem[root.right]:
                return findDeepest(root.left)

            return findDeepest(root.right)

        return findDeepest(root)


root = '[3,5,1,6,2,0,8,null,null,7,4]'
root = TreeNode.fromStrList(root)
root.travel()
out = Solution().subtreeWithAllDeepest(root)
out.travel()
