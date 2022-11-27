from collections import deque
from typing import List


# 不知道是哪个
class Solution1:
    def findLadders(self, beginWord: str, endWord: str,
                    wordList: List[str]) -> int:
        wordList.append(beginWord)

        if endWord not in wordList:
            return []
        dic = dict()
        levelLog = {word: 5000 for word in wordList}
        before = {word: [] for word in wordList}

        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '*' + word[i + 1:]

                if key in dic.keys():
                    dic[key].append(word)
                else:
                    dic[key] = [word]

        queue = [(beginWord, 1)]
        levelLog[beginWord] = 1
        stopLevel = 5000

        while len(queue) > 0:
            item = queue[0]
            del queue[0]
            level = item[1] + 1

            if level > stopLevel:
                break

            for i in range(len(item[0])):
                key = item[0][:i] + '*' + item[0][i + 1:]

                for neighbor in dic[key]:
                    if levelLog[neighbor] == 5000:
                        levelLog[neighbor] = level
                        before[neighbor].append(item[0])

                        if neighbor == endWord:
                            stopLevel = level
                        queue.append((neighbor, level))
                    elif levelLog[neighbor] == level and item[0] not in before[
                            neighbor]:
                        before[neighbor].append(item[0])

        def getAll(word):
            if word == beginWord:
                return [[beginWord]]
            out = []

            for b in before[word]:
                out += [path + [word] for path in getAll(b)]

            return out

        return getAll(endWord)


# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# sl=Solution()
# print(sl.findLadders(beginWord,endWord,wordList))


class Solution:
    def findLadders(self, beginWord: str, endWord: str,
                    wordList: List[str]) -> List[str]:
        if endWord not in wordList:
            return []

        if beginWord not in wordList:
            wordList.append(beginWord)

        dic = dict()

        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '*' + word[i + 1:]

                if key in dic.keys():
                    dic[key].append(word)
                else:
                    dic[key] = [word]

        before = {k: "" for k in wordList}
        queue = deque([(beginWord, 0)])
        level = 0
        find = False

        while len(queue) > 0:
            word, level = queue.popleft()

            if level > 5000:
                return []

            for i in range(len(word)):
                key = word[:i] + '*' + word[i + 1:]

                for neighbor in dic[key]:
                    if neighbor == word:
                        continue

                    if before[neighbor] == "":
                        before[neighbor] = word
                    else:
                        continue

                    if neighbor == endWord:
                        find = True

                        break
                    queue.append((neighbor, level + 1))

                if find:
                    break

            if find:
                break

        if not find:
            return []
        res = []
        tmp = endWord

        while tmp != beginWord:
            res.append(tmp)
            tmp = before[tmp]
        res.append(tmp)

        return res[::-1]


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log"]
beginWord = "hot"
endWord = "dog"
wordList = ["hot", "dog"]

print(Solution().findLadders(beginWord, endWord, wordList))
