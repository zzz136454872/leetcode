from typing import List


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l=0
        r=0
        t_count=0
        f_count=0
        out=0
        for l in range(len(answerKey)):
            while t_count<k and f_count<k and r<len(answerKey):
                if answerKey[r]>
                r+=1
                    
