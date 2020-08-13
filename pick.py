# 黑名单中的随机数 710

from typing import *
import random

class Solution:
    def __init__(self, N: int, blacklist: List[int]):
        self.dict={}
        self.now=1
        blacklist=set(blacklist)
        self.length=N
        self.blacklist=blacklist
        c=0
        whitelist=set()
        for i in range(N):
            if i not in blacklist:
                whitelist.add(i)
                c+=1
                if c>min(len(blacklist)+1,100000):
                    break
        back=whitelist.copy()
        for i in blacklist:
            self.dict[i]=back.pop()
            if len(back)==0:
                back=whitelist.copy()

    def rand(self):
        self.now=(self.now*359753)%183389
        return self.now%self.length

    def pick(self) -> int:
        tmp=self.rand()
        if tmp in self.blacklist:
            return self.dict[tmp]
        return tmp

sl=Solution(2,[])
sl=Solution(1000000000, [640145908])
for i in range(100):
    print(sl.pick())

class Solution1:
    def __init__(self, N: int, blacklist: List[int]):
        blacklist=set(blacklist)
        self.blacklist=blacklist
        self.length=N
    def pick(self) -> int:
        tmp=random.randint(0,self.length-1)
        while tmp in self.blacklist:
            tmp=(tmp+1)%self.length
        return tmp


