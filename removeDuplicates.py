from typing import *

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        counter=[]
        count=0
        for letter in s:
            stack.append(letter)
            if len(stack)==1:
                count=1
            elif letter==stack[-2]:
                count+=1
                if count==k:
                    stack=stack[:-k]
                    if len(stack)>0:
                        count=counter.pop()
            else:
                counter.append(count)
                count=1
        return ''.join(stack)
s = "deeedbbcccbdaa"
k = 3
sl=Solution()
print(sl.removeDuplicates(s,k))
            
