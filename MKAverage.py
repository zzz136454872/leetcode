from heapq import heappush,heappop
from collections import deque


class MKAverage:

    def __init__(self, m: int, k: int):
        self.m=m
        self.k=k
        self.d=m-2*k

        self.top=[]
        self.dtop=[]
        self.bottom=[]
        self.dbottom=[]

        self.s=0
        self.q=deque()

    def addElement(self, num: int) -> None:
        self.q.append(num)

        if self.q.append(num):
            return 
        

    def calculateMKAverage(self) -> int:
        if len(self.q)<m:
            return -1
        return return self.s//self.d



