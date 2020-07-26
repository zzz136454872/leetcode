from typing import *

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix)==0 or len(matrix[0])==0:
            return 0
        graph=[[] for i in range(len(matrix)*len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                num=i*len(matrix[0])+j
                if i>0 and matrix[i-1][j]<matrix[i][j]:
                    graph[num].append(num-len(matrix[0]))
                if j>0 and matrix[i][j]>matrix[i][j-1]:
                    graph[num].append(num-1)
                if i<len(matrix)-1 and matrix[i+1][j]<matrix[i][j]:
                    graph[num].append(num+len(matrix[0]))
                if j<len(matrix[0])-1 and matrix[i][j]>matrix[i][j+1]:
                    graph[num].append(num+1)
        depth=[0 for i in range(len(graph))]
        print(graph)
        def get_depth(i):
            if depth[i]>0:
                return depth[i]
            now=0
            for loc in graph[i]:
                now=max(now,get_depth(loc))
            now+=1
            depth[i]=now
            return now
        for i in range(len(graph)):
            if depth[i]==0:
                depth[i]=get_depth(i)
        print(depth)
        return max(depth)
nums = [ [3,4,5], [3,2,6], [2,2,1] ] 
sl=Solution()
print(sl.longestIncreasingPath(nums))
        

                    
