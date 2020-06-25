from typing import *

class Node:
    def __init__(self):
        self.have=False
        self.next=[None for i in range(26)]

def getord(c):
    return ord(c)-ord('a')

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root=Node()
        max_len=0
        for word in wordDict:
            max_len=max(max_len,len(word))
            word = word[::-1]
            tmp=root
            for c in word:
                c=getord(c)
                if tmp.next[c]==None:
                    tmp.next[c]=Node()
                tmp=tmp.next[c]
            tmp.have=True
        log=[False for i in range(len(s)+1)]
        log[0]=True
        for i in range(1,len(s)+1):
            tmp=root
            for j in range(i-1,max(-1,i-max_len-1),-1):
                if tmp.next[getord(s[j])]==None:
                    break
                tmp=tmp.next[getord(s[j])]
                if tmp.have and log[j]:
                    log[i]=True
                    break

        return log[-1]
s= "leetcode"
s='xiashi'
wordDict = ["leet", "code"]
wordDict=['xiash','i']
sl=Solution()

print(sl.wordBreak(s,wordDict))

