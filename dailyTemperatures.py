from typing import *

#hash map
class Solution1:
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

#Monotonous stack
class Solution:
    def dailyTemperatures(self,T):
        stack=[]
        out=[0 for i in T]
        for day in range(len(T)-1,-1,-1):
            temp=T[day]
            while len(stack)>0 and stack[0][0]<=temp:
                del stack[0]
            if len(stack)==0:
                out[day]=0
            else:
                out[day]=stack[0][1]-day
            stack.insert(0,[temp,day])
        return out

sl=Solution()
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
out=sl.dailyTemperatures(temperatures)
print(out)
                

