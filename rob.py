from typing import *

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         log = [0 for i in range(len(nums))]
#         m=0
#         for i in range(len(nums)):
#             if i<=1:
#                 log[i]=nums[i]
#             else:
#                 log[i]=nums[i]+max(log[:i-1])
#             m=max(m,log[i])
#         return m
# inp=[2,1,1,2]
# sl=Solution()
# print(sl.rob(inp))

# 337
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sum1(a):
    if a in sum1.log.keys():
        return sum1.log[a]
    if a==None:
        sum1.log[a]=0
        return 0
    add1=a.val+sum2(a.left)+sum2(a.right)
    add2=sum1(a.left)+sum1(a.right)
    m=max(add1,add2)
    sum1.log[a]=m
    return m

def sum2(a):
    if a in sum2.log.keys():
        return sum2.log[a]
    if a==None:
        sum2.log[a]=0
        return 0
    m=sum1(a.left)+sum1(a.right)
    sum2.log[a]=m
    return m

class Solution:
    def rob(self, root: TreeNode) -> int:
        sum1.log={}
        sum2.log={}
        return sum1(root)

sl=Solution()
root=TreeNode(3)
root.left=TreeNode(4)
root.right=TreeNode(5)
root.left.left=TreeNode(1)
root.left.right=TreeNode(3)
root.right.right=TreeNode(1)
print(sl.rob(root))
