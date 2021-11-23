from typing import List


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        diff = []
        mem = {}

        for i in range(len(s)):
            mem[s[i]] = mem.get(s[i], 0) + 1

            if s[i] != goal[i]:
                diff.append(i)

                if len(diff) > 2:
                    return False

        if len(diff) == 1:
            return False

        if len(diff) == 0:
            if any([i if i > 1 else 0 for i in mem.values()]):
                return True

            return False

        if s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]:
            return True

        return False


s = "ab"
goal = "ba"
s = "ab"
goal = "ab"
s = "aa"
goal = "aa"
s = "aaaaaaabc"
goal = "aaaaaaacb"
print(Solution().buddyStrings(s, goal))
