from typing import *

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        total=[]
        for i in range(len(nums)):
            for num in nums[i]:
                total.append((num,i))
        total.sort(key=lambda x:x[0])
        log=[0 for i in nums]
        start=0
        end=0
        tmp_start=0
        tmp_end=len(total)-1
        while end<=len(total):
            if 0 in log:
                if end<len(total):
                    log[total[end][1]]+=1
                    end+=1
                else:
                    break
            if not 0 in log:
                if total[end-1][0]-total[start][0]<total[tmp_end][0]-total[tmp_start][0]:
                    tmp_start=start
                    tmp_end=end-1
                log[total[start][1]]-=1
                start+=1
        return [total[tmp_start][0],total[tmp_end][0]]

inp=[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
inp=[[1,3,5,7,9,10],[2,4,6,8,10]]
sl=Solution()
print(sl.smallestRange(inp))

            
