from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        mem1 = {}
        mem2 = {}

        for word in s1.split():
            mem1[word] = mem1.get(word, 0) + 1

        for word in s2.split():
            mem2[word] = mem2.get(word, 0) + 2
        out = []

        for word in mem1:
            if mem1[word] == 1 and mem2.get(word, 0) == 0:
                out.append(word)

        for word in mem2:
            if mem2[word] == 2 and mem1.get(word, 0) == 0:
                out.append(word)

        return out


s1 = "this apple is sweet"
s2 = "this apple is sour"
print(Solution().uncommonFromSentences(s1, s2))
