from typing import List
from collections import deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n=len(arr)
        if n==1:
            return 0
        links=[[] for i in range(n)]
        mem={}
        for i in range(n):
            if i>0:
                links[i].append(i-1)
                links[i-1].append(i)
            if i<n-1:
                links[i].append(i+1)
                links[i+1].append(i)
            if arr[i] in mem:
                for tmp in mem[arr[i]]:
                    links[tmp].append(i)
                    links[i].append(tmp)
                mem[arr[i]].append(i)
            else:
                mem[arr[i]]=[i]
        queue=deque([(0,0)])
        visited=[False]*n
        visited[0]=True
        while len(queue)>0:
            now=queue.popleft()
            loc=now[0]
            dis=now[1]
            for nxt in links[loc]:
                if visited[nxt]:
                    continue
                if nxt==n-1:
                    return dis+1
                visited[nxt]=True
                queue.append((nxt,dis+1))
        return -1 # not going here


arr = [100,-23,-23,404,100,23,23,23,3,404]
arr = [7]
arr = [7,6,9,6,9,6,9,7]
arr = [6,1,9]
arr = [11,22,7,7,7,7,7,7,7,22,13]
print(Solution().minJumps(arr))
