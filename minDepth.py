
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        def minDep(root):
            if root.left==None:
                if root.right==None:
                    return 1
                return minDep(root.right)+1
            else:
                if root.right==None:
                    return minDep(root.left)+1
                return min(minDep(root.left),minDep(root.right))+1
        return minDep(root)

sl=Solution()
root=TreeNode(1)
root.left=TreeNode(2)
print(sl.minDepth(root))

                

