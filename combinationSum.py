from typing import *

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        out=[]
        candidates.sort()
        def find(target,min_num):
            out=[]
            for num in candidates:
                if num < min_num:
                    continue
                if target>num:
                    tmp=find(target-num,num)
                    for l in tmp:
                        out.append([num]+l)
                elif target==num:
                    out.append([num])
                else:
                    break
            return out
        return find(target,-1)

candidates = [2,3,6,7]
target = 7
sl=Solution()
print(sl.combinationSum(candidates,target))
        
