from typing import *

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        def l2n(a):
            return ord(a)-ord('a')
        log={}
        for word in words:
            tmp=['0' for i in range(26)]
            for l in word:
                tmp[l2n(l)]='1'
            if tmp.count('1')>7:
                continue
            tmp=int(''.join(tmp[::-1]),2)
            if tmp not in log.keys():
                log[tmp]=1
            else:
                log[tmp]+=1
        out=[]
        # print(log)
        for puzzle in puzzles:
            # print(puzzle)
            mask=0
            now=0
            for l in puzzle[1:]:
                mask|=1<<l2n(l)
            tmp=mask
            fm=1<<(l2n(puzzle[0]))
            while tmp!=0:
                # # print(tmp)
                t=tmp|fm
                if t in log:
                    now+=log[t]
                tmp=(tmp-1)&mask
            t=tmp|fm
            if t in log:
                now+=log[t]
            out.append(now)
        return out

sl=Solution()
words = ["aaaa","asas","able","ability","actt","actor","access"]
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
print(sl.findNumOfValidWords(words,puzzles))
                



