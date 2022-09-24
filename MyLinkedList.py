class Node:
    def __init__(self, val, prev=None, nxt=None):
        self.val = val
        self.nxt = nxt
        self.prev = prev


class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def show(self):
        return
        p = self.head.nxt

        while p.val != -1:
            print(p.val, end=' ')
            p = p.nxt
        print()

    def revShow(self):
        return
        p = self.tail.prev

        while p.val != -1:
            print(p.val, end=' ')
            p = p.prev
        print()

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        p = self.head.nxt

        for i in range(index):
            p = p.nxt

        return p.val

    def addAtHead(self, val: int) -> None:
        self.size += 1
        newNode = Node(val, self.head, self.head.nxt)
        self.head.nxt = newNode
        newNode.nxt.prev = newNode
        self.show()
        self.revShow()

    def addAtTail(self, val: int) -> None:
        self.size += 1
        newNode = Node(val, self.tail.prev, self.tail)
        self.tail.prev = newNode
        newNode.prev.nxt = newNode
        self.show()

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        if index < 0:
            self.addAtHead(val)

            return
        p = self.head

        for i in range(index):
            p = p.nxt
        self.size += 1
        newNode = Node(val, p, p.nxt)
        p.nxt = newNode
        newNode.nxt.prev = newNode
        self.show()
        self.revShow()

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        p = self.head.nxt

        for i in range(index):
            p = p.nxt
        p.prev.nxt = p.nxt
        p.nxt.prev = p.prev
        self.size -= 1
        self.show()
        self.revShow()


# linkedList = MyLinkedList();
# linkedList.addAtHead(1);
# linkedList.addAtTail(3);
# linkedList.addAtIndex(1,2);
# print(linkedList.get(1)            )
# linkedList.deleteAtIndex(1);
# print(linkedList.get(1))
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


opList = [
    "MyLinkedList", "addAtHead", "addAtHead", "addAtHead", "addAtIndex",
    "deleteAtIndex", "addAtHead", "addAtTail", "get", "addAtHead",
    "addAtIndex", "addAtHead"
]
dataList = [[], [7], [2], [1], [3, 0], [2], [6], [4], [4], [4], [5, 0], [6]]

Tester(opList, dataList)
