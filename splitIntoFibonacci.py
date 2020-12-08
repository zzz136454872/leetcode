from typing import *

class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        max_int=2**31-1
        for i in range(1,len(S)-1):
            if S[0]=='0' and i>1:
                return []
            for j in range(i+1,len(S)):
                if S[i]=='0' and j>i+1:
                    break
                sub1=int(S[:i])
                sub2=int(S[i:j])
                log=[sub1,sub2]
                # print(log)
                pointer=j
                match=True
                while pointer<len(S):
                    log.append(log[-1]+log[-2])
                    tmp=str(log[-1])
                    if(log[-1]>max_int):
                        match=False
                        break
                    flag=True
                    for num in tmp:
                        if pointer<len(S) and num==S[pointer]:
                            pointer+=1
                        else:
                            flag=False
                            break
                    if not flag:
                        match=False
                        break
                if match:
                    return log
        return []

sl=Solution()
inp="11235813"
print(sl.splitIntoFibonacci(inp))
