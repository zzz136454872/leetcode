class Node:
    def __init__(self, val, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.nxt = nxt


class MyCircularDeque:
    def __init__(self, k: int):
        self.size = 0
        self.maxSize = k
        self.front = Node(-1)
        self.rear = Node(-1)
        self.front.nxt = self.rear
        self.rear.prev = self.front

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.size += 1
        newNode = Node(value, self.front, self.front.nxt)
        self.front.nxt.prev = newNode
        self.front.nxt = newNode

        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.size += 1
        newNode = Node(value, self.rear.prev, self.rear)
        self.rear.prev.nxt = newNode
        self.rear.prev = newNode

        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        self.front.nxt.nxt.prev = self.front
        self.front.nxt = self.front.nxt.nxt

        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        self.rear.prev.prev.nxt = self.rear
        self.rear.prev = self.rear.prev.prev

        return True

    def getFront(self) -> int:
        return self.front.nxt.val

    def getRear(self) -> int:
        return self.rear.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.maxSize


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
    "MyCircularDeque", "insertLast", "insertLast", "insertFront",
    "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"
]
dataList = [[3], [1], [2], [3], [4], [], [], [], [4], []]
opList = [
    "MyCircularDeque", "insertFront", "deleteLast", "getRear", "getFront",
    "getFront", "deleteFront", "insertFront", "insertLast", "insertFront",
    "getFront", "insertFront"
]
dataList = [[4], [9], [], [], [], [], [], [6], [5], [9], [], [6]]
Tester(opList, dataList)
