from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        table=[]
        def dfs(root,x,y,table):
            if root==None:
                return 
            table.append((x,y,root.val))
            dfs(root.left,x-1,y-1,table)
            dfs(root.right,x+1,y-1,table)
        dfs(root,0,0,table)
        table.sort()
        if len(table)==0:
            return []
        out=[[table[0][2]]]
        for i in range(1,len(table)):
            if table[i][0]==table[i-1][0]:
                out[-1].append(table[i][2])
            else:
                out.append([table[i][2]])
        return out

        
