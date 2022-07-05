class Tester:
    def __init__(self, opList, dataList):
        testedClass = eval(opList[0])
        testedInstance = testedClass(*dataList[0])

        for i in range(1, len(opList)):
            print(opList[i], dataList[i])

            if not dataList[i]:
                print(getattr(testedInstance, opList[i])())
            else:
                print(getattr(testedInstance, opList[i])(*dataList[i]))


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        print(self)
        print()

    @classmethod
    def travel(cls, head):  # 从head开始遍历
        if head is None:
            print('empty linked list')

            return

        while head is not None:
            print(head.val, end=' ')
            head = head.next
        print()

    def __str__(self):
        return '<' + __name__ + '.ListNode object at 0x{:016X}'.format(
            id(self)) + ' val=' + str(self.val) + '>'


class MyCalendar:
    def __init__(self):
        self.head = ListNode((-1, -1))

    def book(self, start: int, end: int) -> bool:
        p = self.head

        while p.next != None and p.next.val[0] < start:
            p = p.next
        # print(p)

        if p.val[1] > start:
            return False

        if p.next != None and p.next.val[0] < end:
            return False
        q = p.next
        p.next = ListNode((start, end))
        p.next.next = q
        # ListNode.travel(self.head)

        return True


opList = ["MyCalendar", "book", "book", "book"]
dataList = [[], [10, 20], [15, 25], [20, 30]]
Tester(opList, dataList)
