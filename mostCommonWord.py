from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ban = "!?',;."

        for b in ban:
            paragraph = paragraph.replace(b, ' ')
        words = paragraph.split()
        counter = dict()

        for word in words:
            word = word.lower()
            counter[word] = counter.get(word, 0) + 1
        table = list(counter.items())
        banned = set(banned)
        table.sort(key=lambda x: -x[1])

        for pair in table:
            if pair[0] not in banned:
                return pair[0]

        return ""


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(Solution().mostCommonWord(paragraph, banned))
