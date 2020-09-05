from typing import *

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        if endWord not in wordList:
            return []
        dic=dict()
        levelLog={word:5000 for word in wordList}
        before={word:[] for word in wordList}

        for word in wordList:
            for i in range(len(word)):
                key=word[:i]+'*'+word[i+1:]
                if key in dic.keys():
                    dic[key].append(word)
                else:
                    dic[key]=[word]

        queue=[(beginWord,1)]
        levelLog[beginWord]=1
        stopLevel=5000

        while len(queue)>0:
            item=queue[0]
            del queue[0]
            level=item[1]+1
            if level>stopLevel:
                break
            for i in range(len(item[0])):
                key=item[0][:i]+'*'+item[0][i+1:]
                for neighbor in dic[key]:
                    if levelLog[neighbor]==5000:
                        levelLog[neighbor]=level
                        before[neighbor].append(item[0])
                        if neighbor==endWord:
                            stopLevel=level
                        queue.append((neighbor,level))
                    elif levelLog[neighbor]==level and item[0] not in before[neighbor]:
                        before[neighbor].append(item[0])

        def getAll(word):
            if word==beginWord:
                return [[beginWord]]
            out=[]
            for b in before[word]:
                out+=[path+[word] for path in getAll(b)]
            return out

        return getAll(endWord)


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

sl=Solution()
print(sl.findLadders(beginWord,endWord,wordList))



