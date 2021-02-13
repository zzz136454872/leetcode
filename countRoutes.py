from typing import *

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dis=[[abs(locations[i]-locations[j]) \
                for j in range(len(locations))]\
                for i in range(len(locations))]
        mem=[[[-1 for k in range(fuel+1)]\
                for j in range(len(locations))]\
                for i in range(len(locations))]
        mod=10**9+7
        def findPath(loc1,loc2,fuel):
            # print('in')
            if fuel<0:
                return 0
            if mem[loc1][loc2][fuel]!=-1:
                return mem[loc1][loc2][fuel]
            out=0
            if loc1==finish:
                out+=1
            for i in range(len(locations)):
                if i!=loc1:
                    out=(out+findPath(i,loc2,fuel-dis[loc1][i]))%mod
            mem[loc1][loc2][fuel]=out
            # print(loc1,loc2,out,fuel)
            return out
        return findPath(start,finish,fuel)

sl=Solution()
locations = [1,2,3]
start = 0
finish = 2
fuel = 40
print(sl.countRoutes(locations,start,finish, fuel))
