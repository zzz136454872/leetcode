# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def travel(self,order='pre'):
        # order : pre,mid,post
        if order!='pre' and order!='mid' and order!='post':
            print('order error: ',order)
        self.travel_sub(order)
        print()

    def travel_sub(self,order):
        if order=='pre':
            print(self.val, end=' ')
        if self.left!=None:
            self.left.travel_sub(order)
        if order=='mid':
            print(self.val, end=' ')
        if self.right!=None:
            self.right.travel_sub(order)
        if order=='post':
            print(self.val, end=' ')

if __name__=='__main__':
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    root.left.left=TreeNode(4)
    root.travel(order='post')

