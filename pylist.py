class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def travel(cls, head):  # 从head开始遍历
        if head is None:
            print('empty linked list')

            return
        mem = set()

        while head is not None:
            mem.add(head)
            print(head.val, end=' ')
            head = head.next

            if head in mem:
                print('loop from', head.val, end='')

                break
        print()

    @classmethod
    def fromList(cls, nums):
        virtual_head = ListNode(12345)
        p = virtual_head

        for num in nums:
            p.next = ListNode(num)
            p = p.next

        return virtual_head.next

    def __str__(self):
        return '<' + __name__ + '.ListNode object at 0x{:016X}'.format(
            id(self)) + ' val=' + str(self.val) + '>'

    def getTail(self):
        p = self

        while p.next != None:
            p = p.next

        return p
