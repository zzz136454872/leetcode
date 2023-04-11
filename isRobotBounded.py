from typing import List


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        loc = [0, 0]
        p = 0
        m = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for c in instructions:
            if c == "G":
                loc[0] += m[p][0]
                loc[1] += m[p][1]
            elif c == 'L':
                p = (p + 3) % 4
            else:
                p = (p + 1) % 4

        return loc == [0, 0] or p != 0


instructions = "GGLLGG"
instructions = "GG"
instructions = "GL"
print(Solution().isRobotBounded(instructions))
