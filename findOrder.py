from typing import *

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        log1=dict()
        log2=dict()
        for i in prerequisites:
            if i[0] in log1.keys():
                log1[i[0]].append(i[1])
            else:
                log1[i[0]]=[i[1]]
            
            if i[1] in log2.keys():
                log2[i[1]].append(i[0])
            else:
                log2[i[1]]=[i[0]]

        out=[]
        for i in range(numCourses):
            if i not in log1.keys():
                out.append(i)
                if i in log2.keys():
                    tmp=log2.pop(i)
                    for j in tmp:
                        log1[j].remove(i)

        while len(out)<numCourses:
            changed=False
            l=list(log1.keys())
            for i in l:
                if len(log1[i])==0:
                    out.append(i)
                    log1.pop(i)
                    changed=True
                    if i in log2.keys():
                        tmp=log2.pop(i)
                        for j in tmp:
                            log1[j].remove(i)
            if not changed:
                return []
        return out
            
num=4
inp=[[1,0],[2,0],[3,1],[3,2]]  
sl=Solution()
print(sl.findOrder(num,inp))


            
            
