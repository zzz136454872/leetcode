from typing import *
from heapq import *

# 不知道是哪个
class Solution1:
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


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic=dict()
        for word in words:
            dic[word]=dic.get(word,0)+1
        log=list(dic.items())
        log.sort(key=lambda x:(-x[1],x[0]))
        return [x[0] for x in log[:k]]
            
sl=Solution()
words=["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 3
words=['i','love','leetcode','i','love','coding']
words=['i','love','leetcode','i','love','coding']
print(sl.topKFrequent(words,k))
