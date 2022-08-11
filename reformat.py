from typing import List


class Solution:
    def reformat(self, s: str) -> str:
        number = []
        letter = []

        for l in s:
            if l.isdigit():
                number.append(l)
            else:
                letter.append(l)

        if abs(len(number) - len(letter)) > 1:
            return ""

        if len(number) > len(letter):
            number, letter = letter, number
        res = []

        while len(number) > 0:
            res.append(letter.pop())
            res.append(number.pop())

        if len(letter) > 0:
            res.append(letter.pop())

        return "".join(res)


s = "a0b1c2"
s = "leetcode"
s = "1229857369"
print(Solution().reformat(s))
