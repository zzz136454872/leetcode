from typing import *

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.log={}
        if node==None:
            return None
        return self.getNode(node)
        
    def getNode(self,node):
        if node.val in self.log.keys():
            return self.log[node.val]
        newNode=Node()
        newNode.val=node.val
        self.log[node.val]=newNode
        for neighbor in node.neighbors:
            newNode.neighbors.append(self.getNode(neighbor))
        return newNode

        
