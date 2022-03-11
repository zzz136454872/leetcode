class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        root.depth = 1
        self.getDepth(root)

        while p.depth > q.depth:
            p = p.father

        while p.depth < q.depth:
            q = q.father

        while p != q:
            p = p.father
            q = q.father

        return p

    def getDepth(self, p):
        if p.left != None:
            p.left.father = p
            p.left.depth = p.depth + 1
            self.getDepth(p.left)

        if p.right != None:
            p.right.father = p
            p.right.depth = p.depth + 1
            self.getDepth(p.right)
