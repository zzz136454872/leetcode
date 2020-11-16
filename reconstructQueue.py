from typing import *
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x:(-x[0],x[1]))
        #print(people)
        log=[]
        for man in people:
            log.insert(man[1],man)
        return log

people=[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
sl=Solution()
print(sl.reconstructQueue(people))
            
