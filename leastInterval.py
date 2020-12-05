from typing import *

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if len(tasks)==0:
            return 0
        if n==0:
            return len(tasks)
        log={}
        for l in tasks:
            log[l] = log[l]+1 if l in log.keys() else 1
        log=sorted(list(log.values()),key=lambda x:-x)
        equal=0
        for i in range(1,len(log)):
            if log[i]==log[0]:
                equal+=1
            else:
                break
        table=[1 for i in range(log[0])]
        now=0
        for i in range(1,len(log)):
            for j in range(log[i]):
                table[now]+=1
                now=(now+1)%len(table)
        out=0
        rest=0
        for i in range(len(table)-1):
            add=max(table[i],n+1)
            out+=add
            rest+=add-table[i]
        out+=1+equal
        addition=table[-1]-1-equal
        out+=max(0,addition-rest)
        return out

sl=Solution()
inp=["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
print(sl.leastInterval(inp,n))

