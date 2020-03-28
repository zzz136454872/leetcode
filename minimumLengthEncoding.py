from typing import *

class Node:
    def __init__(self):
        self.dic=[None for i in range(26)]
        self.count=0

    def verify(self):
        for i in self.dic:
            if i!=None:
                return False
        if self.count>0:
            return False
        self.count+=1
        return True

def reverseList(word):
    return list(word)[::-1]

def char2Int(letter):
    return ord(letter)-ord('a')

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        head=Node()
        for word in words:
            word=reverseList(word)
            now=head
            for letter in word:
                if now.dic[char2Int(letter)]==None:
                    tmp=Node()
                    now.dic[char2Int(letter)]=tmp
                    now=tmp
                else:
                    now=now.dic[char2Int(letter)]
        out=''
        for word in words:
            wordList=reverseList(word)
            now=head
            for letter in wordList:
                now=now.dic[char2Int(letter)]
            if now.verify():
                out+=word+'#'
        return len(out)

sl=Solution()
words = ["time", "me", "bell","time"]
print(sl.minimumLengthEncoding(words))



            
            
