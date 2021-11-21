# 二叉树的最大深度
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# 多叉树的最大深度
from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0

        if len(root.children) == 0:
            return 1
        else:
            return 1 + max([self.maxDepth(child) for child in root.children])
