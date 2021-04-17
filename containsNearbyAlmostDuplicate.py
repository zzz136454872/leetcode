from typing import *

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if not nums or not k:
            return False
        k=min(k,len(nums-1))
        
        minValue=-2**31
        
        def getID(a):
            return (a-minValue)//(t+1)
        
        buckets={}

        for i in range(k+1):
            bid=getID(nums[i])
            if bid in buckets.keys():
                if len(buckets[bid])>0:
                    return True
                buckets[bid].append(nums[i])
            else:
                buckets[bid]=[nums[i]]
            for tmp in buckets.get(bid-1,[]):
                if abs(tmp-nums[i])<=t:
                    return True
            for tmp in buckets.get(bid+1,[]):
                if abs(tmp-nums[i])<=t:
                    return True

        for i in range(k+1,len(nums)):
            del_bid=getID(nums[i-k-1])
            buckets[del_bid].pop(0)
            bid=getID(nums[i])
            if bid in buckets.keys():
                if len(buckets[bid])>0:
                    return True
                buckets[bid].append(nums[i])
            else:
                buckets[bid]=[nums[i]]
            for tmp in buckets.get(bid-1,[]):
                if abs(tmp-nums[i])<=t:
                    return True
            for tmp in buckets.get(bid+1,[]):
                if abs(tmp-nums[i])<=t:
                    return True
        return False

sl=Solution()
nums = [1]
k = 1
t = 1
print(sl.containsNearbyAlmostDuplicate(nums,k,t))

