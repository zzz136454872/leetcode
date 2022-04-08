class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            tmp = s[i:] + s[:i]

            if tmp == goal:
                return True

        return False
