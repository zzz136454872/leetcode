from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        out = ""

        for letter in letters:
            if ord(letter) > ord(target) and (out == ""
                                              or ord(out) > ord(letter)):
                out = letter

        if len(out) == 1:
            return out
        out = 'z'

        for letter in letters:
            if ord(out) > ord(letter):
                out = letter

        return out


letters = ["c", "f", "j"]
target = "j"
print(Solution().nextGreatestLetter(letters, target))
