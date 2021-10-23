from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        a = int(area**0.5) + 1

        while area % a != 0:
            a -= 1

        return [max(area // a, a), min(area // a, a)]
