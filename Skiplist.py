from typing import *
from random import randint

class SkipListNode:
    def init(self,val,level,maxLevel):
        self.val=val
        self.count==1
        self.level=level
        self.next=[None]*(maxLevel-level)

class Skiplist:
    def __init__(self):
        self.maxLevel=13
        self.head=SkipListNode(-1,0,13)

    def searchNode(self,target):
        nowNode=self.head
        while nowNode!=None:
            i=0
            while i<len(nowNode.next) and nowNode.next[i]!=None and nowNode.next[i].val>target:
                i+=1
            if i==len(nowNode.next):
                return False
            else:
                nowNode=nowNode.next[i]
                if nowNode.val==target:
                    return nowNode
        return None

    def search(self, target: int) -> bool:
        if self.searchNode(target):
            return True
        return False

    def add(self, num: int) -> None:
        tmp=self.searchNode(num)
        if tmp:
            tmp.count+=1
            return 
        level=self.getLevel()
        prev=[None]*(self.maxLevel-level)
        nxt=[None]*(self.maxLevel-level)

    def erase(self, num: int) -> bool:
        tmp=self.searchNode(num)
        if not tmp:
            return False
        tmp.count-=1
        if tmp.count>0:
            return 

    def getLevel(self):
        level=self.maxLevel-1
        while randint(0,1)==1 and level>0:
            level-=1
        return level

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)

sl=Skiplist()
test={}
for i in range(20000):
    tmp=sl.getLevel()
    test[tmp]=test.get(tmp,0)+1

print(sorted(test.items()))

# A Hacked Solution

class Skiplist:

    def __init__(self):
        self.mem=[0]*(2*10**4+5)


    def search(self, target: int) -> bool:
        return self.mem[target]>0


    def add(self, num: int) -> None:
        self.mem[num]+=1


    def erase(self, num: int) -> bool:
        if self.mem[num]==0:
            return False
        self.mem[num]-=1
        return True

