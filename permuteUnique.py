class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used=[False for i in nums]
        nums.sort()
        out=[]
        def dfs(path,depth):
            if depth==len(nums):
               out.append(path.copy())
               return
            i=0
            for i in range(len(nums)):
                if used[i]==1:
                    continue
                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                used[i]=True
                path.append(nums[i])
                dfs(path, depth+1)
                used[i]=False
                path.pop()
        dfs([],0)
        return out
