class Solution:
    def majorityElement(self, nums) :
        log=dict()
        for num in nums:
            if num in log.keys():
                log[num]+=1
            else:
                log[num]=0
        for key in log.keys():
            if log[key]>=len(nums)/2:
                return key
        return 0
                

        
