from typing  import *

class Trie:
    def __init__(self):
        self.next=[None for i in range(26)]
        self.index=-1
        self.include=[]

class Solution:

    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        def isPalindrome(s):
            i=0
            j=len(s)-1
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        
        def l2i(a):
            return ord(a)-ord('a')

        n=len(words)
        suffix=[[] for i in range(n)]
        root=Trie()

        for i in range(n):
            tmp=root
            for j in range(len(words[i])):
                if isPalindrome(words[i][j:]):
                    suffix[i].append(j)
                letter=l2i(words[i][j])
                if tmp.next[letter]==None:
                    tmp.next[letter]=Trie()
                tmp=tmp.next[letter]
                tmp.include.append(i)
            tmp.index=i
        out=[]

        for i in range(n):
            tmp=root
            for j in range(len(words[i])-1,-1,-1):
                letter=l2i(words[i][j])
                if tmp.next[letter]!=None:
                    tmp=tmp.next[letter]
                else:
                    break
                if tmp.index!=-1:
                    if isPalindrome(words[i][:j]) and i!=tmp.index:
                        #print('flag1',tmp.index,i)
                        out.append([tmp.index,i])
        return out

sl=Solution()
inp=["abcd","dcba","lls","s","sssll"]
inp=['a','']
print(sl.palindromePairs(inp))





        
