class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        out = 0

        for letter in s:
            if letter == 'R':
                balance += 1
            else:
                balance -= 1

            if balance == 0:
                out += 1
            print(out, letter)

        return out


s = "RLRRLLRLRL"
s = "RLLLLRRRLR"
s = "RLRRRLLRLL"
print(Solution().balancedStringSplit(s))
