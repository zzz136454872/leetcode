from pytree import TreeNode


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        num = -1

        def travel(root):
            if root is None:
                return
            nonlocal num

            if root.val != num:
                if num == -1:
                    num = root.val
                else:
                    num = -2

                    return
            travel(root.left)
            travel(root.right)

        travel(root)

        return num != -2


sl = Solution()
root = '[1,1,1,1,1,null,1]'
root = '[2,2,2,5,2]'
root = TreeNode.fromStrList(root)
print(sl.isUnivalTree(root))
