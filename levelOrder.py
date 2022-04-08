from pyNode import Node


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 层序遍历
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        out = []

        if root == None:
            return []
        src = [root]

        while len(src) != 0:
            dst = []
            level = []

            while len(src) != 0:
                node = src.pop(0)

                if node.left != None:
                    dst.append(node.left)

                if node.right != None:
                    dst.append(node.right)
                level.append(node.val)
            out.append(level)
            src = dst

        return out


# N叉树的层序遍历
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        out = []

        if root is None:
            return out
        queue = [root]

        while len(queue) > 0:
            out.append([])
            new_queue = []

            for node in queue:
                out[-1].append(node.val)

                if node.children is None:
                    continue

                for nn in node.children:
                    new_queue.append(nn)
            queue = new_queue

        return out
