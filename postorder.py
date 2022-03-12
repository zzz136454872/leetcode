from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        out = []

        def po(root):
            if root is None:
                return

            if root.children is not None:
                for c in root.children:
                    po(c)
            out.append(root.val)

        po(root)

        return out


print(Solution().postorder(root))
