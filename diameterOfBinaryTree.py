class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root==None:
            return 0
        self.log(root)
        return self.get_dis(root,0)

    def log(self,root):
        if root.left!=None:
            self.log(root.left)
        if root.right!=None:
            self.log(root.right)
        if root.left==None:
            root.left_end=0
        else:
            root.left_end=max(root.left.left_end,root.left.right_end)+1
        if root.right==None:
            root.right_end=0
        else:
            root.right_end=max(root.right.left_end,root.right.right_end)+1

    def get_dis(self,root,max_dis):
        if root.left!=None:
            max_dis=max(max_dis,self.get_dis(root.left,max_dis))
        if root.right!=None:
            max_dis=max(max_dis,self.get_dis(root.right,max_dis))
        max_dis=max(max_dis,root.left_end+root.right_end)
        return max_dis

