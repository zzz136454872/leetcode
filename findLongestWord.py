from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def match(s1, s2):
            j = 0

            for i in range(len(s1)):
                if s1[i] == s2[j]:
                    j += 1

                    if j == len(s2):
                        return True

            return False

        out = ''

        for word in dictionary:
            if match(s, word):
                if len(word) > len(out):
                    out = word
                elif len(word) == len(out) and word < out:
                    out = word

        return out


s = "abpcplea"
dictionary = ["ale", "apple", "monkey", "plea"]
s = "abpcplea"
dictionary = ["b", "a", "c"]
print(Solution().findLongestWord(s, dictionary))
