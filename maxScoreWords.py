
from typing import *

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def add(a,b):
            return [a[i]+b[i] for i in range(len(a))]
        
        def sub(a,b):
            return [a[i]-b[i] for i in range(len(b))]

        def greater(a,b):
            return False not in [a[i]>=b[i] for i in range(len(a))]
        
        def l2n(a):
            return ord(a)-ord('a')

        def n2l(a):
            return chr(a+ord('a'))
        
        def w2s(word):
            return sum([score[l2n(l)] for l in word])
        
        def word2list(word):
            return [word.count(n2l(i)) for i in range(26)]

        scoresWord=[w2s(word) for word in words]
        weightWords=[word2list(word) for word in words]
        print(weightWords)
        weights=word2list(''.join(letters))
        self.maxScore=0
        n=len(words)

        def getScore(level,score,weight):
            if level==n:
                self.maxScore=max(self.maxScore,score)
                return 

            getScore(level+1,score,weight)
            if greater(weight,weightWords[level]):
                weight=sub(weight,weightWords[level])
                getScore(level+1,score+scoresWord[level],weight)

        getScore(0,0,weights)
        return self.maxScore

words = ["dog","cat","dad","good"]
letters = ["a","a","c","d","d","d","g","o","o"]
score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
sl=Solution()
print(sl.maxScoreWords(words,letters,score))
