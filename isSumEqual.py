from typing import *

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def l2n(a):
            return str(ord(a)-ord('a'))
        
        def trans(word):
            out=''
            for letter in word:
                out+=l2n(letter)
            return int(out)
            
        f=trans(firstWord)
        s=trans(secondWord)
        t=trans(targetWord)
        return f+s==t

firstWord = "aaa"
secondWord = "a"
targetWord = "aaaa"
firstWord = "aaa"
secondWord = "a"
targetWord = "aab"
firstWord = "acb"
secondWord = "cba"
targetWord = "cdb"
sl=Solution()
print(sl.isSumEqual(firstWord,secondWord,targetWord))
        
