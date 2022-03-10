class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        out = []

        def pre(root):
            if root is None:
                return
            out.append(root.val)

            for c in root.children:
                pre(c)

        pre(root)

        return out
