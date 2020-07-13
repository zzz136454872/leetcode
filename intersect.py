from typing import *

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1=dict()
        for num in nums1:
            if num in dict1.keys():
                dict1[num]+=1
            else:
                dict1[num]=1
        dict2=dict()
        for num in nums2:
            if num in dict2.keys():
                dict2[num]+=1
            else:
                dict2[num]=1

        out=[]
        for num in dict1.keys():
            if num in dict2.keys():
                out.extend([num]*min(dict1[num],dict2[num]))
        return out

sl=Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(sl.intersect(nums1,nums2))

            
