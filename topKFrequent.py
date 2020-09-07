from typing import *
from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=dict()
        for num in nums:
            if num in dic.keys():
                dic[num]+=1
            else:
                dic[num]=1
        heap=list()
        out=[]
        for num in dic.keys():
            if len(heap)<k:
                heappush(heap,(dic[num],num))
            else:
                if dic[num]>heap[0][0]:
                    heappop(heap)
                    heappush(heap,(dic[num],num))
        return [i[1] for i in heap]

nums = [1,1,1,2,2,3]
k = 2

sl=Solution()
print(sl.topKFrequent(nums,k))
