from typing import *

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        temp_day=[100000 for i in range(102)]
        out=[0 for i in T]

        for day in range(len(T)-1,-1,-1):
            temp=T[day]
            temp_day[temp]=day
            last=min(temp_day[temp+1:])
            if last<100000:
                out[day]=last-day
            else:
                out[day]=0
        return out
sl=Solution()
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
out=sl.dailyTemperatures(temperatures)
print(out)
                

