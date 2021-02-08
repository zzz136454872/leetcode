from typing import *

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        n=len(word1)+len(word2)
        out=[]
        for _ in range(n):
            if word1>word2:
                out.append(word1[0])
                word1=word1[1:]
            else:
                out.append(word2[0])
                word2=word2[1:]
        return ''.join(out)

sl=Solution()
word1 = "cabaa"
word2 = "bcaaa"
word1 = "abcabc"
word2 = "abdcaba"
print(sl.largestMerge(word1,word2))
