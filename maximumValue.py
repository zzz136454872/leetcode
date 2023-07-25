from typing import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        def value(s):
            if s.isdigit():
                return int(s)

            return len(s)

        return max(value(s) for s in strs)
