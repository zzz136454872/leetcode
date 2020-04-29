# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def __init__(self,data):
        self.data=data
    def get(self, index: int) -> int:
        return self.data[index]
    def length(self) -> int:
        return len(self.data)

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        self.log=dict()
        self.mountain=mountain_arr
        l=0
        length=mountain_arr.length()-1
        r=length
        if target<self.get(0) and target<self.get(r):
            #print('err')
            return -1
        while l<r-1:
            m1=(2*l+r)//3
            m2=(l+2*r)//3
            v1=self.get(m1)
            v2=self.get(m2)
            if v1<v2:
                l=m1+1
            else:
                r=m2-1
        if(self.get(l)>self.get(r)):
            m_loc=l
        else:
            m_loc=r
        print(m_loc)
        if target> self.get(m_loc):
            return -1
        l=0
        r=m_loc
        while l<=r:
            m=(l+r)//2
            v=self.get(m)
            if v>target:
                r=m-1
            elif v<target:
                l=m+1
            else:
                return m
        l=m_loc
        r=length
        while l<=r:
            m=(l+r)//2
            v=self.get(m)
            if v>target:
                l=m+1
            elif v<target:
                r=m-1
            else:
                return m
        return -1

    def get(self,i):
        if i in self.log.keys():
            return self.log[i]
        tmp=self.mountain.get(i)
        self.log[i]=tmp
        return tmp
inp=[0,5,3,1]
target=1

moun=MountainArray(inp)
sl=Solution()
print(sl.findInMountainArray(target,moun))
        
           
            
