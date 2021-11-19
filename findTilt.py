from pytree import TreeNode


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def find(root):

            if root is None:
                return (0, 0)
            lo = find(root.left)
            ro = find(root.right)

            return (abs(lo[1] - ro[1]) + lo[0] + ro[0],
                    lo[1] + ro[1] + root.val)

        return find(root)[0]


root = '[1,2,3]'
root = '[4,2,9,3,5,null,7]'
root = '[21,7,14,1,1,2,2,3,3]'

root = TreeNode.fromStrList(root)
print(Solution().findTilt(root))
