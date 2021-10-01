from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = set()
        end = set()

        for path in paths:
            if path[0] in end:
                end.remove(path[0])
            else:
                start.add(path[0])

            if path[1] in start:
                start.remove(path[1])
            else:
                end.add(path[1])

        return end.pop()


paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
paths = [["B", "C"], ["D", "B"], ["C", "A"]]
paths = [["A", "Z"]]
print(Solution().destCity(paths))
