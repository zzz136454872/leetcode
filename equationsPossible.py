from typing import *

class Solution:
    ord_a=ord('a')
    def equationsPossible(self, equations: List[str]) -> bool:
        self.log=[i for i in range(26)]
        for e in equations:
            a=self.parser(e)
            if a[1]=='=':
                self.merge(a[0],a[2])
        #print(self.log)

        for e in equations:
            a=self.parser(e)
            if a[1]=='!':
                if self.find(a[0])==self.find(a[2]):
                    return False
        return True

    def find(self,a):
        if self.log[a]==a:
            return a
        self.log[a]=self.find(self.log[a])
        return self.log[a]

    def merge(self,a,b):
        fa=self.find(self.log[a])
        fb=self.find(self.log[b])
        if fa!=fb:
            self.log[fa]=fb

    def parser(self,a):
        return (ord(a[0])-Solution.ord_a,
                a[1],
                ord(a[3])-Solution.ord_a)
sl=Solution()
equation=["a==b","b!=a"]
print(sl.equationsPossible(equation))
