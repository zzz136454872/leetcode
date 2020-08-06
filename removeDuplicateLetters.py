from typing import *

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        def l2i(a):
            return ord(a)-ord('a')
        stack=[]
        count=[0 for i in range(26)]
        for letter in s:
            count[l2i(letter)]+=1
        for letter in s:
            if letter not in stack:
                while len(stack)>0 and l2i(stack[-1])>l2i(letter) and count[l2i(stack[-1])]>0:
                    stack.pop()
                stack.append(letter)
            count[l2i(letter)]-=1
        return ''.join(stack)

sl=Solution()
s="bcabc"
print(sl.removeDuplicateLetters(s))

