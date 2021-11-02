from pylist import ListNode


class Solution:
    def deleteNode(self, node):
        while node.next is not None:
            node.val = node.next.val
            pre = node
            node = node.next
        pre.next = None


head = [4, 5, 1, 9]
node = 5
head = [1, 2, 3, 4]
node = 3
head = [-3, 5, -99]
node = -3
root = ListNode.fromList(head)
Solution().deleteNode(root)
ListNode.travel(root)
