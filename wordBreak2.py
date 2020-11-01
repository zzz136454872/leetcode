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
            tmp=root
            for c in word:
                c=getord(c)
                if tmp.next[c]==None:
                    tmp.next[c]=Node()
                tmp=tmp.next[c]
            tmp.have=True
        log=[[] for i in range(len(s))]
        for i in range(len(s)):
            tmp=root
            j=i
            while tmp!=None and j<len(s):
                c=getord(s[j])
                if tmp.next[c]!=None:
                    tmp=tmp.next[getord(s[j])]
                    j+=1
                else:
                    break
                if tmp.have:
                    log[i].append(j)
        out=[]
        print(log)
        buffer_list=[[] for i in range(len(s))]
        flag_list=[True for i in range(len(s))]

        def dfs(loc):
            if loc==len(s):
                return [[loc]]
            if len(buffer_list[loc])>0:
                return buffer_list[loc]
            if not flag_list[loc]:
                return []
            out=[]
            for next_loc in log[loc]:
                tmp=dfs(next_loc)
                for sub in tmp:
                    out.append([loc]+sub)
            if len(out)==0:
                flag_list[loc]=False
            else:
                buffer_list[loc]=out
            print(loc,out)
            return out
                    
        solution=dfs(0)
        print(buffer_list)
        print(flag_list)
        out=[]
        for tmp in solution:
            tmp2=[]
            for i in range(len(tmp)-1):
                tmp2.append(s[tmp[i]:tmp[i+1]])
            out.append(' '.join(tmp2))
        return out

s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
s="aaaaaaa"
wordDict=["aaaa","aaa"]
sl=Solution()
print(sl.wordBreak(s,wordDict))

