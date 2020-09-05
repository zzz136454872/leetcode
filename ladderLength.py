from typing import *

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        if endWord not in wordList:
            return 0
        if beginWord==endWord:
            return 1
        dic=dict()
        visited=dict()

        for word in wordList:
            for i in range(len(word)):
                key=word[:i]+'*'+word[i+1:]
                if key in dic.keys():
                    dic[key].append(word)
                else:
                    dic[key]=[word]
            visited[word]=False

        queue=[(beginWord,1)]
        visited[beginWord]=True

        while len(queue)>0:
            item=queue[0]
            del queue[0]
            level=item[1]+1
            for i in range(len(item[0])):
                key=item[0][:i]+'*'+item[0][i+1:]
                for neighbor in dic[key]:
                    if not visited[neighbor]:
                        visited[neighbor]=True
                        if neighbor==endWord:
                            return level
                        queue.append((neighbor,level))
        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

sl=Solution()
print(sl.ladderLength(beginWord,endWord,wordList))



