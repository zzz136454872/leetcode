from pytree import TreeNode


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if B is None:
            return False

        def same(r1, r2):
            if r2 is None:
                return True

            if r1 is None:
                return False

            if r1.val != r2.val:
                return False

            return same(r1.left, r2.left) and same(r1.right, r2.right)

        def dfs(root):
            if root is None:
                return False

            if same(root, B):
                return True

            if dfs(root.left):
                return True

            return dfs(root.right)

        return dfs(A)


A = '[1,2,3]'
B = '[3,1]'

A = '[3,4,5,1,2]'
B = '[4,1]'

A = TreeNode.fromStrList(A)
B = TreeNode.fromStrList(B)
print(Solution().isSubStructure(A, B))
