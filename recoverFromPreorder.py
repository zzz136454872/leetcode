from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        print('s',S)
        if len(S)==0:
            return None
        if not '-' in S:
            num=int(S)
            root=TreeNode(num)
            return root
        loc=S.index('-')
        num=int(S[:loc])
        S=S[loc:]
        root=TreeNode(num)
        i=1
        while i<len(S):
            if i<len(S)-1 and S[i-1]!='-' and S[i]=='-' and S[i+1] !='-':
                break
            else:
                i+=1
        left=S[:i]
        right=S[i:]
        print('left',left)
        print('right',right)
        left=self.trim(left)
        right=self.trim(right)
        root.left=self.recoverFromPreorder(left)
        root.right=self.recoverFromPreorder(right)
        return root
    
    def trim(self,string):
        string=list(string)
        i=1
        while i<len(string):
            if string[i]!='-' and string[i-1]=='-':
                del string[i-1]
            else:
                i+=1
        return ''.join(string)

sl=Solution()
inp="1-2--3---4-5--6---7"
root=sl.recoverFromPreorder(inp)
print(root.val)
print(root.left.val)
print(root.right.val)
print(root.right.left.val)

