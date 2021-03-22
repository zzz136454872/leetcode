from typing import *

class TrieNode:
    def __init__(self):        
        self.child = [None, None]
        self.cnt = 0
 
def insertTrie(root, N):
    for i in range(15, -1, -1):
        x = bool( (N) & (1 << i));
        if(root.child[x] == None):
            root.child[x] = TrieNode();
        root.child[x].cnt += 1;
        root= root.child[x]; 
   
def cntSmaller(root, N, K):
    cntPairs = 0;
    for i in range(15, -1, -1):      
        if(root == None):
            break
        x = bool(N & (1 << i))
        y = K & (1 << i);
        if (y != 0):
            if (root.child[x]):
                cntPairs += root.child[ x].cnt
            root = root.child[1 - x];
        else:
            root = root.child[x]
    return cntPairs;
  
def cntSmallerPairs(arr, K):
    root = TrieNode();
    cntPairs = 0;
    for i in range(len(arr)):
        cntPairs += cntSmaller(root, arr[i], K);
        insertTrie(root, arr[i]);    
    return cntPairs

class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        return cntSmallerPairs(nums,high+1)-cntSmallerPairs(nums,low)

sl=Solution()
nums = [1,4,2,7]
low = 2
high = 6
print(sl.countPairs(nums,low,high))
  
