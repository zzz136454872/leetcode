from typing import *
import copy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def get_tree(start,end):
    if start>end:
        return [None]
    out=[]
    for i in range(start,end+1):
        p=TreeNode(i)
        left=get_tree(start,i-1)
        right=get_tree(i+1,end)
        for l in left:
            for r in right:
                p.left=l
                p.right=r
                out.append(copy.deepcopy(p))
                #out.append(p)
    return out

def print_trees(al):
    for a in al:
        print_tree(a)
        print()

def print_tree(a):
    if a==None:
        return 
    print(a.val)
    print_tree(a.left)
    print_tree(a.right)

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n==0:
            return []
        return get_tree(1,n)
            
sl=Solution()
out=sl.generateTrees(0)
print_trees(out)

