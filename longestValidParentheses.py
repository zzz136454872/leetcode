from typing import *

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        log=[]
        for i in range(len(s)-1):
            if s[i]=='(' and s[i+1]==')':
                log.append([i,i+1])
        
        changed=True
        while changed:
            changed=False
            i=0
            while i < len(log):
                #print(log[i])
                #print(log[i][0]-1)
                if log[i][0]>0 and s[log[i][0]-1]=='(' \
                        and log[i][1] < len(s)-1 and s[log[i][1]+1]==')':
                    log[i][0]-=1
                    log[i][1]+=1
                    changed=True
                if i < len(log)-1 and log[i][1]==log[i+1][0]-1:
                    end=log[i+1][1]
                    del log[i+1]
                    log[i][1]=end
                    changed=True
                i+=1
        max_len=0
        for cut in log:
            max_len=max(max_len,cut[1]-cut[0]+1)
        return max_len
        
sl=Solution()
s="))))())()()(()"
print(sl.longestValidParentheses(s))

