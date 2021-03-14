from typing import *
import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        out=0
        n=len(classes)
        for c in classes:
            out+=c[0]/c[1]

        class C:

            def __init__(self,not_pass,total):
                self.not_pass=not_pass
                self.total=total
                self.score=self.not_pass/((self.total+1)*self.total)
            
            def __lt__(self,anotherC):
                return self.score>anotherC.score
            
            def __str__(self):
                return 'not_pass:'+str(self.not_pass)\
                        +' total:'+str(self.total)\
                        +' score:'+str(self.score)
        
        l=[C(c[1]-c[0],c[1]) for c in classes]
        heapq.heapify(l)

        for i in range(extraStudents):
            now=heapq.heappop(l)
            out+=now.score
            # print(now)
            # print(out)
            new=C(now.not_pass,now.total+1)
            heapq.heappush(l,new)

        # print(n)
        return out/n

classes = [[1,2],[3,5],[2,2]]
extraStudents = 2
classes = [[2,4],[3,9],[4,5],[2,10]]
extraStudents = 4
sl=Solution()
print(sl.maxAverageRatio(classes,extraStudents))

                
