from typing import *
import heapq

# 构建邻接表
# 计算距离
# 排序
# 遍历邻接表
# 返回结果

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        # 构建邻接表
        at=[[] for i in range(n+1)]
        for edge in edges:
            at[edge[0]].append((edge[1],edge[2]))
            at[edge[1]].append((edge[0],edge[2]))
        
        # 计算距离
        dist=[1234567890 for i in range(n+1)]
        dist[n]=0
        heap=[n]
        while len(heap)>0:
            p=heapq.heappop(heap)
            dist_now=dist[p]
            for nextp,dist_next in at[p]:
                if dist_next+dist_now<dist[nextp]:
                    dist[nextp]=dist_next+dist_now
                    heapq.heappush(heap,nextp)

        # for p in at[n]:
        #     dist[p[0]]=p[1]
        # for point_count in range(n-1):
        #     now_loc=0
        #     now_dis=1234567890
        #     for i in range(1,n):
        #         if not visited[i] and now_dis>dist[i]:
        #             now_dis=dist[i]
        #             now_loc=i
        #     visited[now_loc]=True
        #     # print(now_loc,now_dis,visited,dist)
        #     for p in at[now_loc]:
        #         dist[p[0]]=min(dist[p[0]],now_dis+p[1])

        # print(dist)

        # 排序
        order=[(dist[i],i) for i in range(1,len(dist))]
        order.sort()

        # print(order)

        # 遍历邻接表
        times=[0 for i in range(n+1)]
        times[n]=1
        mod=10**9+7

        for d,p in order[1:]:
            tmp=0
            for nextp in at[p]:
                if dist[p]>dist[nextp[0]]:
                    tmp=(tmp+times[nextp[0]])%mod
            times[p]=tmp
        # print(times)
        return times[1]

sl=Solution()
n = 7
edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]
n = 5
edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
print(sl.countRestrictedPaths(n,edges))

