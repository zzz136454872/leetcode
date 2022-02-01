class Solution:
    def numberOfSteps(self, num: int) -> int:
        out = 0

        while num != 0:
            out += 1

            if num % 2 != 0:
                num -= 1
            else:
                num //= 2

        return out
