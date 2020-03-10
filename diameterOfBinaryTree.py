class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return get_dis(root,0)

    def log(root):
        if root.left!=None:
            log(root.left)
        if root.right!=None:
            log(root.right)
        if root.left==None:
            root.left_end=0
        else:
            root.left=max(root.left.left_end,root.left.right_end)+1
        if root.right_end==None:
            right=0
        else:
            root.right=max(root.right.left_end,root.right.right_end)+1

    def get_dis(root,max_dis):
        if root.left!=None:
            max_dis=max(max_dis,get_dis(root.left,max_dis))
        if root.right!=None:
            max_dis=max(max_dis,get_dis(root.right,max_dis))
        max_dis=max(max_dis,root.left_end+root.right_end)
        return max_dis




