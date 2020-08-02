from typing import *

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        total=sum(rods)
        valid=[False for i in range(total+1)]
        valid[0]=True
        min_waste=[1234567 for i in range(total+1)]
        min_waste[0]=0
        for rod in rods:
            for i in range(total,-1,-1):
                print(rod,i,min_waste)
                if i>=rod and valid[i-rod]:
                    min_waste[i]=min(min_waste[i],min_waste[i-rod]+rod)
                    valid[i]=True
                if i>=2*rod and valid[i-2*rod]:
                    min_waste[i]=min(min_waste[i],min_waste[i-2*rod])
                    valid[i]=True
        return (total-min_waste[total])//2

#rods=[1,2,3,4,5,6]
rods=[1,2]
sl=Solution()
print(sl.tallestBillboard(rods))

