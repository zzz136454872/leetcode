from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str,
                               words: List[str]) -> str:
        def l2n(a):
            return ord(a) - ord('a')

        def l2id(lic):
            out = [0 for i in range(26)]

            for letter in lic:
                if letter.isalpha():
                    out[l2n(letter.lower())] += 1

            return out

        def include(a, b):
            for i in range(26):
                if a[i] < b[i]:
                    return False

            return True

        mem = l2id(licensePlate)
        outP = -1

        for i in range(len(words)):
            memNow = l2id(words[i])

            if include(memNow, mem):
                if outP == -1 or len(words[i]) < len(words[outP]):
                    outP = i

        if outP >= 0:
            return words[outP]

        return ''


licensePlate = "1s3 PSt"
words = ["step", "steps", "stripe", "stepple"]
licensePlate = "1s3 456"
words = ["looks", "pest", "stew", "show"]
licensePlate = "OgEu755"
words = [
    "enough", "these", "play", "wide", "wonder", "box", "arrive", "money",
    "tax", "thus"
]

print(Solution().shortestCompletingWord(licensePlate, words))
