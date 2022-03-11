# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        out = []

        if root == None:
            return []
        src = [root]

        while len(src) != 0:
            dst = []
            level = []

            while len(src) != 0:
                node = src.pop(0)

                if node.left != None:
                    dst.append(node.left)

                if node.right != None:
                    dst.append(node.right)
                level.append(node.val)
            out.append(level)
            src = dst

        return out
