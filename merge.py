from typing import *

class Solution1:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        i=0
        while i<len(intervals)-1:
            if intervals[i][1]>=intervals[i+1][0]:
                tmp=[intervals[i][0],max(intervals[i+1][1],intervals[i][1])]
                del intervals[i]
                del intervals[i]
                intervals.insert(i,tmp)
            else:
                i+=1
        return intervals

# inp=[[1,3],[2,6],[8,10],[15,18]]
# sl=Solution()
# print(sl.merge(inp))
            
# 合并两个有序数组
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums12=nums1[:m]
        p1=0
        p2=0
        while p1<m or p2<n:
            if p2==n:
                nums1[p1+p2]=nums12[p1]
                p1+=1
                continue
            if p1==m:
                nums1[p1+p2]=nums2[p2]
                p2+=1
                continue
            if nums12[p1]<nums2[p2]:
                nums1[p1+p2]=nums12[p1]
                p1+=1
            else:
                nums1[p1+p2]=nums2[p2]
                p2+=1

sl=Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
sl.merge(nums1,m,nums2,n)
print(nums1)
            
            


            
        

