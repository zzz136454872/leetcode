from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str],
                              words: List[str]) -> List[int]:
        def f(s):
            count = 0
            tmp = 'z'

            for letter in s:
                if ord(letter) < ord(tmp):
                    count = 1
                    tmp = letter
                elif letter == tmp:
                    count += 1

            return count

        # print(queries)
        mem = [[f(queries[i]), i, 0] for i in range(len(queries))]
        # print(mem)
        mem.sort()
        # print(mem)
        words = [f(s) for s in words]
        words.sort(reverse=True)

        for i in range(len(mem)):
            while len(words) > 0 and words[-1] <= mem[i][0]:
                words.pop()
            mem[i][2] = len(words)
        mem.sort(key=lambda x: x[1])

        return [x[2] for x in mem]


queries = ["cbd"]
words = ["zaaaz"]
queries = ["bbb", "cc"]
words = ["a", "aa", "aaa", "aaaa"]
print(Solution().numSmallerByFrequency(queries, words))
