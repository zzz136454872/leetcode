from typing import List

def dec(func):
    def wrap(*args):
        out=func(*args)
        print(args,out)
        return out
    return wrap


# TLE
class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n=len(graph)
        threshold=2*n**2+1
        mem=[[[-1]*threshold for i in range(n)] for k in range(n)]
        print('threshold',threshold)

        @dec
        def dfs(m,c,k):
            # print(m,c,k)
            if m==0:
                return 1
            if m==c:
                return 2
            if k>=threshold:
                return 0
            out=mem[m][c][k]
            if out!=-1:
                return out
            if k%2==0:
                out=2
                for np in graph[m]:
                    tmp=dfs(np,c,k+1)
                    if tmp==1:
                        out=1
                        break
                    if tmp==0:
                        out=0
            else:
                out=1
                if m==3 and c==2 and k==1:
                    print('now')
                for np in graph[c]:
                    if np==0:
                        continue
                    tmp=dfs(m,np,k+1)
                    if tmp==2:
                        out=2
                        break
                    if tmp==0:
                        out=0
            mem[m][c][k]=out
            return out
        return dfs(1,2,0)

graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
# graph = [[1,3],[0],[3],[0,2]]
# graph = [[2,3],[3,4],[0,4],[0,1],[1,2]]
graph=[[3,4],[3,5],[3,6],[0,1,2],[0,5,6],[1,4],[2,4]]
print(Solution().catMouseGame(graph))

        
