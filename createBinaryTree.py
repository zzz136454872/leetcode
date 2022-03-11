# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self,
                         descriptions: List[List[int]]) -> Optional[TreeNode]:
        mem = {}
        hasParent = set()

        for d in descriptions:
            if d[0] not in mem:
                mem[d[0]] = TreeNode(d[0])

            if d[1] not in mem:
                mem[d[1]] = TreeNode(d[1])
            hasParent.add(d[1])

            if d[2]:
                mem[d[0]].left = mem[d[1]]
            else:
                mem[d[0]].right = mem[d[1]]
        print(hasParent)
        print(mem)

        for k in mem:
            if k not in hasParent:
                return mem[k]

        return None


descriptions = [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0],
                [80, 19, 1]]
print(Solution().createBinaryTree(descriptions).val)
