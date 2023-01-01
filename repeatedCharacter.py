from collections import defaultdict


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        mem = defaultdict(int)

        for letter in s:
            mem[letter] += 1

            if mem[letter] == 2:
                return letter

        return 'a'
