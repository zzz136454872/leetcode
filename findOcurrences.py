from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split()
        out = []

        for i in range(2, len(text)):
            if text[i - 2] == first and text[i - 1] == second:
                out.append(text[i])

        return out


text = "alice is a good girl she is a good student"
first = "a"
second = "good"
text = "we will we will rock you"
first = "we"
second = "will"
print(Solution().findOcurrences(text, first, second))
