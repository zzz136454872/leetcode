
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        return self.diff(root)[2]

    def diff(self,root):
        #print(root.val,root.left.val if root.left!=None else None,
        #        root.right.val if root.right!=None else None)
        if root.left==None and root.right==None:
            return (root.val,root.val,0)
        maxval=root.val
        minval=root.val
        maxdiff=0
        if root.left!=None:
            out=self.diff(root.left)
            maxval=max(out[0],maxval)
            minval=min(out[1],minval)
            maxdiff=max(maxval-root.val,root.val-minval,out[2])
        #print(maxdiff)
        if root.right!=None:
            out=self.diff(root.right)
            maxval=max(out[0],maxval)
            minval=min(out[1],minval)
            maxdiff=max(maxval-root.val,root.val-minval,out[2],maxdiff)
        out=(maxval,minval,maxdiff) 
        #print(out)
        return out

sl=Solution()
head=TreeNode(0)
head.left=TreeNode(3)
#head.left=p
head.right=TreeNode(10)
#p.right=head
#head=p
p=TreeNode(8)
q=head
head=TreeNode(2)
head.left=q
head.right=p
#p.right=head
#head=p

print(sl.maxAncestorDiff(head))
#2 0 8
#0 3 10
#3 4 None
#4 5 None
#5 None None
#(5, 4, 1)
#(5, 3, 2)
#10 None None
#(10, 0, 10)
#8 7 1
#7 None None
#1 None 6
#6 9 None
#9 None None
#(9, 6, 3)
#(9, 1, 8)
#(9, 1, 8)
#(10, 0, 8)
