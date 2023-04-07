from typing import List


class Trie:
    def __init__(self):
        self.next = [None for i in range(26)]
        self.have = False


def l2i(a):
    return ord(a) - ord('a')


class StreamChecker:
    def __init__(self, words: List[str]):
        self.log = Trie()
        self.maxLen = 0
        self.queue = ''

        for word in words:
            tmp = self.log
            self.maxLen = max(self.maxLen, len(word))

            for letter in word[::-1]:
                letter = l2i(letter)

                if tmp.next[letter] == None:
                    tmp.next[letter] = Trie()
                tmp = tmp.next[letter]
            tmp.have = True

    def query(self, letter: str) -> bool:
        self.queue = letter + self.queue

        if len(self.queue) > 3 * self.maxLen:
            self.queue = self.queue[:self.maxLen]
        tmp = self.log

        for letter in self.queue:
            letter = l2i(letter)
            tmp = tmp.next[letter]

            if tmp == None:
                return False

            if tmp.have:
                return True
        print('error')

        return False


streamChecker = StreamChecker(["cd", "f", "kl"])
# 初始化字典
print(streamChecker.query('a'))  # 返回 false
print(streamChecker.query('b'))  # 返回 false
print(streamChecker.query('c'))  # 返回 false
print(streamChecker.query('d'))  # 返回 true，因为 'cd' 在字词表中
print(streamChecker.query('e'))  # 返回 false
print(streamChecker.query('f'))  # 返回 true，因为 'f' 在字词表中
print(streamChecker.query('g'))  # 返回 false
print(streamChecker.query('h'))  # 返回 false
print(streamChecker.query('i'))  # 返回 false
print(streamChecker.query('j'))  # 返回 false
print(streamChecker.query('k'))  # 返回 false
print(streamChecker.query('l'))  # 返回 true，因为 'kl' 在字词表中。
