from typing import List


class Solution:
    def vowelStrings(self, words: List[str],
                     queries: List[List[int]]) -> List[int]:
        presum = [0]
        o = set(['a', 'e', 'i', 'o', 'u'])
        res = []

        for q in words:
            if q[0] in o and q[-1] in o:
                presum.append(presum[-1] + 1)
            else:
                presum.append(presum[-1])

        for q in queries:
            res.append(presum[q[1] + 1] - presum[q[0]])

        return res


words = ["aba", "bcb", "ece", "aa", "e"]
queries = [[0, 2], [1, 4], [1, 1]]
words = ["a", "e", "i"]
queries = [[0, 2], [0, 1], [2, 2]]
print(Solution().vowelStrings(words, queries))
