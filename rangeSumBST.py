from typing import *
from pytree import TreeNode

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        now_sum=0
        
        def mid_order(root):
            if not root:
                return 
            if root.val>=low:
                mid_order(root.left)
            if root.val>=low and root.val<=high:
                nonlocal now_sum
                now_sum+=root.val
            if root.val<=high:
                mid_order(root.right)

        mid_order(root)
        return now_sum

sl=Solution()
root = '[10,5,15,3,7,13,18,1,null,6]'
low = 6
high = 10
root=TreeNode.fromStrList(root)
print(sl.rangeSumBST(root,low,high))
            
            

