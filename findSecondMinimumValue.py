from pytree import TreeNode


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if root is None:
            return -1

        min_val = root.val
        m = 12345678190000
        second = m

        def dfs(root):
            nonlocal second

            if root is None:
                return

            if root.val > min_val:
                second = min(second, root.val)
            else:
                dfs(root.left)
                dfs(root.right)

        dfs(root)

        return second if second != m else -1


sl = Solution()
root = '[2,2,5,null,null,5,7]'
root = '[2,2,2]'
root = '[1,1,3,1,1,3,4,3,1,1,1,3,8,4,8,3,3,1,6,2,1]'
root = '[2,2,3]'
root = TreeNode.fromStrList(root)
TreeNode.travel(root)
print(sl.findSecondMinimumValue(root))
