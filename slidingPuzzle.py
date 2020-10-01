
from typing import *

class Node:
    def __init__(self,level):
        self.level=level;
        self.next=[None for i in range(6)]

def insert(root,key,level):
    for i in range(6):
        if root.next[key[i]]==None:
            root.next[key[i]]=Node(level)
        root=root.next[key[i]]

def check(root,key):
    for i in range(6):
        if root.next[key[i]]==None:
            return False
        root=root.next[key[i]]
    return True

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        init=board[0]+board[1]
        target=[1,2,3,4,5,0]
        if init==target:
            return 0
        queue=[(init,0)]
        root=Node(0)
        insert(root, init, 0)
        table=[[1,3],[0,2,4],[1,5],[0,4],[1,3,5],[2,4]]
        while len(queue)>0:
            state,level=queue.pop(0)
            level+=1
            empty_loc=state.index(0)
            for n in table[empty_loc]:
                next_state=state.copy()
                next_state[empty_loc]=state[n]
                next_state[n]=state[empty_loc]
                if next_state==target:
                    return level
                if not check(root, next_state):
                    queue.append((next_state,level))
                insert(root,next_state,level)
        return -1

board =[[1,2,3],[5,4,0]]
sl=Solution()
print(sl.slidingPuzzle(board))
