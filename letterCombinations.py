from typing import *

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table=[None,None,'abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        from_list=['']
        to_list=[]
        for digit in digits:
            to_list=[]
            index=int(digit)
            for s in from_list:
                for letter in table[index]:
                    to_list.append(s+letter)
            from_list=to_list
        return to_list
sl=Solution()
print(sl.letterCombinations('23'))
