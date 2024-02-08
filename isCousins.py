from typing import *

from pytree import TreeNode


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_level=-1
        y_level=-1
        x_parent=None
        y_parent=None
        def search(root,level):
            nonlocal x_level,x_parent
            nonlocal y_level,y_parent

            if root is None:
                return 

            if root.left!=None:
                if root.left.val==x:
                    x_level=level+1
                    x_parent=root
                elif root.left.val==y:
                    y_level=level+1
                    y_parent=root
                search(root.left, level+1)

            if root.right!=None:
                if root.right.val==x:
                    x_level=level+1
                    x_parent=root
                elif root.right.val==y:
                    y_level=level+1
                    y_parent=root
                search(root.right, level+1)
        search(root,0)

        if x_level!=-1 and x_level==y_level and x_parent!=y_parent:
            return True

        return False

sl=Solution()
root = '[1,2,3,null,4,null,5]'
root = '[1,2,3,null,4]'
x = 2
y = 3
root=TreeNode.fromStrList(root)
print(sl.isCousins(root,x,y))

