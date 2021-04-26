from pytree import TreeNode


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        out = None
        pre = None

        def midorder(root):
            if root is None:
                return
            midorder(root.left)
            nonlocal pre
            root.left = None

            if pre is not None:
                pre.right = root
            else:
                nonlocal out
                out = root
            pre = root
            midorder(root.right)

        midorder(root)

        return out


inp = '[2,1,4,null,null,3]'
root = TreeNode.fromStrList(inp)
sl = Solution()
out = sl.increasingBST(root)
TreeNode.travel(out)
