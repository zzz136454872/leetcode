from typing import *

class Solution:
    def isValid(self, s: str) -> bool:
        pair={'}':'{',']':'[',')':'('}
        stack=[]
        for bracklet in s:
            if bracklet in pair.keys():
                if len(stack)>0 and stack[-1]==pair[bracklet]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracklet)
        return len(stack)==0
        
