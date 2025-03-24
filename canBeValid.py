# wa


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        x = 0
        y = 0

        for i in range(len(locked)):
            if locked[i] == '0':
                x += 1
                y = max(y - 1, (i + 1) % 2)
            else:
                d = 1 if s[i] == '(' else -1
                x += d
                y = max(y + d, (i + 1) % 2)

            if x < y:
                return False

        return y == 0


s = "))()))"
locked = "010100"
s = "()()"
locked = "0000"
s = ")"
locked = "0"

print(Solution().canBeValid(s, locked))
