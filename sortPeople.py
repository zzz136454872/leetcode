from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [
            a[1] for a in sorted([(-heights[i], names[i])
                                  for i in range(len(names))])
        ]
