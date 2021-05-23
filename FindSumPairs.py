from typing import *

class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        table={}
        for num in nums2:
            table[num]=table.get(num,0)+1
        nums1.sort()
        self.nums1=nums1
        self.nums2=nums2
        self.table=table

    def add(self, index: int, val: int) -> None:
        self.table[self.nums2[index]]-=1
        self.nums2[index]+=val
        self.table[self.nums2[index]]=self.table.get(self.nums2[index],0)+1

    def count(self, tot: int) -> int:
        out=0
        for num in self.nums1:
            if num>=tot:
                return out
            tmp=self.table.get(tot-num,0)
            out+=tmp
            # print(num,tmp,tot-num)
        return out

class Tester:
    def __init__(self,opList,dataList):
        testedClass=eval(opList[0])
        testedInstance=testedClass(*dataList[0])
        for i in range(1,len(opList)):
            if not dataList[i]:
                print(getattr(testedInstance,opList[i])())
            else:
                print(getattr(testedInstance,opList[i])(*dataList[i]))

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)

a=FindSumPairs
opList=["FindSumPairs", "add", "add", "count"]
dataList=[[[9,70,14,9,76],[26,26,58,23,74,68,68,78,58,26]],[6,10],[5,6],[32]]
Tester(opList,dataList)

