from typing import *

mod=10**9+7
def rev(a):
    lk=1
    k=0
    lr=a
    r=mod
    while r!=1:
        t=lr//r
        lr,r=r,lr%r
        lk,k=k,lk-t*k
    return k%mod

class Fancy:
    def __init__(self):
        self.m=1
        self.k=0
        self.data=[]

    def append(self, val: int) -> None:
        val=(val-self.k)%mod
        val=(val*rev(self.m))%mod
        self.data.append(val)

    def addAll(self, inc: int) -> None:
        self.k=(self.k+inc)%mod

    def multAll(self, m: int) -> None:
        self.k=(self.k*m)%mod
        self.m=(self.m*m)%mod

    def getIndex(self, idx: int) -> int:
        if idx>=len(self.data):
            return -1
        return (self.m*self.data[idx]+self.k)%mod

fancy = Fancy();
fancy.append(2);  # 奇妙序列：[2]
fancy.addAll(3);  # 奇妙序列：[2+3] -> [5]
fancy.append(7);  # 奇妙序列：[5, 7]
fancy.multAll(2); # 奇妙序列：[5*2, 7*2] -> [10, 14]
print(fancy.getIndex(0));# 返回 10
fancy.addAll(3);  # 奇妙序列：[10+3, 14+3] -> [13, 17]
fancy.append(10); # 奇妙序列：[13, 17, 10]
fancy.multAll(2); # 奇妙序列：[13*2, 17*2, 10*2] -> [26, 34, 20]
print(fancy.getIndex(0))# 返回 26
print(fancy.getIndex(1))# 返回 34
print(fancy.getIndex(2))# 返回 20
print(fancy.getIndex(2))# 返回 20



