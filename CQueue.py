from typing import *

class CQueue:

    def __init__(self):
        self.q1=[]
        self.q2=[]

    def appendTail(self, value: int) -> None:
        self.q1.append(value)

    def deleteHead(self) -> int:
        if len(self.q2)>0:
            return self.q2.pop()
        while len(self.q1)>0:
            tmp=self.q1.pop()
            self.q2.append(tmp)
        if len(self.q2)>0:
            return self.q2.pop()
        else:
            return -1



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
