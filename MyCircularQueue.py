class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyCircularQueue:
    def __init__(self, k: int):
        self.size = k
        self.front = Node(-1)
        p = self.front

        for i in range(k):
            p.next = Node(-1)
            p = p.next
        p.next = self.front
        self.rear = p
        self.c = 0

    def enQueue(self, value: int) -> bool:
        if self.c == self.size:
            return False
        self.c += 1
        self.rear = self.rear.next
        self.rear.val = value

        return True

    def deQueue(self) -> bool:
        if self.c == 0:
            return False
        self.c -= 1
        self.front = self.front.next

        return True

    def Front(self) -> int:
        if self.c == 0:
            return -1

        return self.front.val

    def Rear(self) -> int:
        if self.c == 0:
            return -1

        return self.rear.val

    def isEmpty(self) -> bool:
        return self.c == 0

    def isFull(self) -> bool:
        return self.c == self.size


m = MyCircularQueue(3)
m.enQueue(1)
m.enQueue(2)
m.enQueue(3)
m.enQueue(4)
print(m.Rear())
