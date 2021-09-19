class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def travel(cls, head):  # 从head开始遍历
        if head is None:
            print('empty linked list')

        while head is not None:
            print(head.val, end=' ')
            head = head.next
        print()

    @classmethod
    def fromList(cls, nums):
        virtual_head = ListNode(12345)
        p = virtual_head

        for num in nums:
            p.next = ListNode(num)
            p = p.next

        return virtual_head.next
