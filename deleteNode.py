from typing import Optional

from pylist import ListNode
from pytree import TreeNode


# 不知道是哪个
class Solution:
    def deleteNode(self, node):
        while node.next is not None:
            node.val = node.next.val
            pre = node
            node = node.next
        pre.next = None


# head = [4, 5, 1, 9]
# node = 5
# head = [1, 2, 3, 4]
# node = 3
# head = [-3, 5, -99]
# node = -3
# root = ListNode.fromList(head)
# Solution().deleteNode(root)
# ListNode.travel(root)


class Solution:
    def deleteNode(self, root: Optional[TreeNode],
                   key: int) -> Optional[TreeNode]:
        find = False

        def travelFind(r):
            nonlocal find

            if r is None or find:
                return r
            print(r.val)

            if r.val == key:
                find = True

                if r.left is None:
                    return r.right

                if r.right is None:
                    return r.left
                tmp = r.right

                if tmp.left is None:
                    tmp.left = r.left

                    return tmp
                prev = r

                while tmp.left != None:
                    prev = tmp
                    tmp = tmp.left
                tmp.left = r.left
                prev.left = tmp.right
                tmp.right = r.right

                return tmp
            else:
                r.left = travelFind(r.left)
                r.right = travelFind(r.right)

                return r

        return travelFind(root)


root = '[5,3,6,2,4,null,7]'
key = 3
root = '[5,3,6,2,4,null,7]'
key = 0
root = '[]'
key = 0
root = TreeNode.fromStrList(root)
out = Solution().deleteNode(root, key)
root.travel('mid')
