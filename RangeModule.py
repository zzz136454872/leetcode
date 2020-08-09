from typing import *

class RangeModule:

    def __init__(self):
        self.store=[]

    def bsearch(self,r):
        start=0
        end=len(self.store)-1
        while start<=end:
            mid=(start+end)//2
            now=self.store[mid]
            if now==r:
                return mid
            elif now>r:
                end=mid-1
            else:
                start=mid+1

    def addRange(self, left: int, right: int) -> None:
        i=self.bsearch([left,right])
        merge=False
        if i>0 and self.store[i-1][1]>=left:
            self.store[i-1][1]=max(self.store[i-1][1],right)
            merge=True
        if i<len(self.store) and right>=self.store[i][0]:
            self.store[i][0]=left
            merge=True
        if not merge:
            self.store.insert(i,[left,right])
        elif i>0 and i<len(self.store) and self.store[i-1][1]>=self.store[i][0]:
            self.store[i-1][1]=self.store[i][1]
            del self.store[i]

    def queryRange(self, left: int, right: int) -> bool:
        i=self.bsearch([left,right])
        if i==len(self.store):
            return False
        if self.store[i][1]>=right:
            return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        i=self.bsearch([left,right])
        if i==len(self.store):
            return 
        if self.store[i][0]<left:
            self.store[i][1]=min(self.store[i][1],left)
        else:

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
