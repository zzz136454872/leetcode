from typing import *

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=[False for i in rooms]
        def visit(a):
            if visited[a]:
                return 
            visited[a]=True
            for room in rooms[a]:
                visit(room)
        visit(0)
        return False not in visited 

sl=Solution()
rooms=[[1],[2],[3],[]]
print(sl.canVisitAllRooms(rooms))
            
        

    
