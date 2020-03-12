class Solution:
    def combinationSum2(self, candidates, target):
        if len(candidates)==0:
            return [[]]
        candidates.sort()
        end=0
        s=0
        out=[]
        log=[]
        while True:
            print(log)
            if s == target:
                out.append(log)
            if s < target:
                s+=candidates[end]
                log.append(candidates[end])
                end+=1
            else:
                s-=log[0]
                log=log[1:]
            if end >= len(candidates):
                break
        return out

inp=[10,1,2,7,6,1,5]
sl=Solution()

print(sl.combinationSum2(inp,8))
        


            
