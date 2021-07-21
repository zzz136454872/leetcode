from pylist import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode,
                            headB: ListNode) -> ListNode:
        p1 = headA
        p2 = headB
        passed = False

        while p1 != p2 or not passed:
            # print('enter',p1.val if p1!=None else None,
            #       p2.val if p2!=None else None)

            if p1 is None:
                p1 = headB
                passed = True
            else:
                p1 = p1.next

            if p2 is None:
                p2 = headA
            else:
                p2 = p2.next
            # print('out  ',p1.val if p1!=None else None,
            #       p2.val if p2!=None else None)

        return p1


sl = Solution()
listA = [4, 1, 8, 4, 5]
listB = [5, 0, 1, 8, 4, 5]
headA = ListNode.fromList(listA)
headB = ListNode.fromList([6, 0, 1])
tailA = headA
tailB = headB
tailB = tailB.next
tailB = tailB.next
tailA = tailA.next
tailA = tailA.next
tailB.next = tailA
ListNode.travel(headA)
ListNode.travel(headB)
out = sl.getIntersectionNode(headA, headB)

if not out:
    print('none')
else:
    print(out.val)
