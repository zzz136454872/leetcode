from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        table = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
            ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
            "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
        ]

        def l2n(a):
            return ord(a) - ord('a')

        def toM(a):
            out = ""

            for letter in a:
                out += table[l2n(letter)]

            return out

        s = set()

        for word in words:
            s.add(toM(word))

        return len(s)


words = ["gin", "zen", "gig", "msg"]
print(Solution().uniqueMorseRepresentations(words))
