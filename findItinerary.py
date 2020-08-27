from typing import *

def dfs(tickets,now):
    if len(tickets)==0:
        return [now]
    for i in range(len(tickets)):
        if tickets[i][0]==now:
            tmp=dfs(tickets[:i]+tickets[i+1:],tickets[i][1])
            if tmp!=None:
                tmp.insert(0,now)
                return tmp
    return None

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        return dfs(tickets,'JFK')

sl=Solution()
tickets=[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(sl.findItinerary(tickets))
                    

