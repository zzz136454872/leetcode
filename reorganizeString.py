from typing import *
class Solution:
    def reorganizeString(self, S: str) -> str:
        log={}
        for l in S:
            if l not in log.keys():
                log[l]=1
            else:
                log[l]+=1
        log=list(log.items())
        log.sort(key=lambda x:-x[1])
        print(log)
        if log[0][1]>(len(S)+1)/2:
            return ''
        tmp=[log[0][0] for i in range(log[0][1])]
        loc=0
        for i in range(1,len(log)):
            for j in range(log[i][1]):
                tmp[loc]+=log[i][0]
                loc=(loc+1)%len(tmp)
        out=''
        for s in tmp:
            out+=s
        return out

sl=Solution()
S="aaab"
print(sl.reorganizeString(S))
