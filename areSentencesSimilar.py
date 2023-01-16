from typing import List


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()

        if len(s1) > len(s2):
            s1, s2 = s2, s1
        c1 = 0
        c2 = len(s1)

        for i in range(len(s1)):
            if s1[i] == s2[i]:
                c1 = i + 1
            else:
                break

        for i in range(len(s1) - 1, -1, -1):
            if s1[i] == s2[i + len(s2) - len(s1)]:
                c2 = i
            else:
                break

        return c1 >= c2


sentence1 = "My name is Haley"
sentence2 = "My Haley"
sentence1 = "of"
sentence2 = "A lot of words"
sentence1 = "Eating right now"
sentence2 = "Eating"
sentence1 = "Luky"
sentence2 = "Lucccky"
print(Solution().areSentencesSimilar(sentence1, sentence2))
