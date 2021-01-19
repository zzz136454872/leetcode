from typing import *

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        total=0
        n=len(points)
        visited=[False for i in range(n)]
        def get_dis(a,b):
            return abs(a[0]-b[0])+abs(a[1]-b[1])
        dis=[[get_dis(points[i],points[j]) 
                    for j in range(n)] 
                for i in range(n)]
        visited[0]=True
        dis_in=[k for k in dis[0]]
        dis_in[0]=0
        loc=0
        for i in range(n-1):
            min_value=100000000
            min_loc=0
            for j in range(n):
                if not visited[j] and dis_in[j]<min_value:
                    min_value=dis_in[j]
                    min_loc=j
            total+=min_value
            dis_in[min_loc]=0
            visited[min_loc]=True
            for j in range(n):
                dis_in[j]=min(dis_in[j],dis[min_loc][j])
        return total

points = [[3,12],[-2,5],[-4,1]] 
sl=Solution()
print(sl.minCostConnectPoints(points))


        

        
