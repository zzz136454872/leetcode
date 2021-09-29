from pytree import TreeNode


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        mem = []

        def travel(root):
            if root is None:
                return
            travel(root.left)
            mem.append(root.val)
            travel(root.right)

        travel(root)

        def buildTree(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            root = TreeNode(mem[mid])
            root.left = buildTree(l, mid - 1)
            root.right = buildTree(mid + 1, r)

            return root

        return buildTree(0, len(mem) - 1)


root = '[1,null,2,null,3,null,4,null,null]'
root = TreeNode.fromStrList(root)
out = Solution().balanceBST(root)
out.travel()
