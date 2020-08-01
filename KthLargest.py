from typing import *

def adjust(nums,index):
    left=2*index+1
    if left>=len(nums):
        return 
    if nums[left]<nums[index]:
        min_loc=left
    else:
        min_loc=index
    right=left+1
    if right<len(nums):
        if nums[right]<nums[min_loc]:
            min_loc=right
    if min_loc!=index:
        nums[index],nums[min_loc]=nums[min_loc],nums[index]
        adjust(nums,min_loc)
        
def push(nums,number):
    loc=len(nums)
    nums.append(number)
    parent=(loc-1)//2
    while nums[loc]<nums[parent]:
        nums[loc],nums[parent]=nums[parent],nums[loc]
        loc=parent

def pop_min(nums):
    if len(nums)==0:
        return -1
    tmp=nums[0]
    nums[0]=nums[-1]
    del nums[-1]
    adjust(nums,0)
    return tmp

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        size=len(nums)
        for i in range((size-1)//2,-1,-1):
            adjust(nums,i)
        while len(nums)>k:
            pop_min(nums)
        self.nums=nums
        self.k=k
        print(self.nums)
        
    def add(self, val: int) -> int:
        if len(self.nums)==self.k and val<=self.nums[0]:
            return self.nums[0]
        push(self.nums,val)
        print(self.nums)
        if len(self.nums)>self.k:
            pop_min(self.nums)
        return self.nums[0]

# Your KthLargest object will be instantiated and called as such:
k = 2;
arr = [0];
kthLargest=KthLargest(k, arr)
print(kthLargest.add(-1))# returns 4
# print(kthLargest.add(1))# returns 5
# print(kthLargest.add(-2))# returns 5
# print(kthLargest.add(-4))# returns 8
# print(kthLargest.add(3))# returns 8

