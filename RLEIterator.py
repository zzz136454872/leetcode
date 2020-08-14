from typing import *

class Node:
    def __init__(self):
        self.count=10**15
        self.next=None
        self.num=-1

class RLEIterator:
    def __init__(self, A: List[int]):
        self.head=None
        self.tail=None
        for i in range(0,len(A),2):
            p=Node()
            p.count=A[i]
            p.num=A[i+1]
            if self.head==None:
                self.head=p
                self.tail=p
            self.tail.next=p
            self.tail=p
        self.tail.next=Node()

    def next(self, n: int) -> int:
        while n>self.head.count:
            n-=self.head.count
            self.head=self.head.next
        self.head.count-=n
        return self.head.num

        

