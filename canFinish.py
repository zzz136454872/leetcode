from typing import *

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        log=[[] for i in range(numCourses)]
        log2=[[] for i in range(numCourses)]
        visited=[False for i in range(numCourses)]
        for depend in prerequisites:
            log[depend[0]].append(depend[1])
            log2[depend[1]].append(depend[0])
        def visit(a):
            visited[a]=True
            for course in log2[a]:
                log[course].remove(a)
                if not visited[course] and len(log[course])==0:
                    visit(course)
        i=0
        while i<numCourses:
            if visited[i]:
                i+=1
                continue
            if log[i]==[]:
                visit(i)
                i=0
            else:
                i+=1
        return not (False in visited)
inp1=3
inp2=[[1,0],[2,1],[0,2]] 
sl=Solution()
print(sl.canFinish(inp1,inp2))



                    
            

    
