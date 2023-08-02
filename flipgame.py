from typing import List


class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        ban = set()

        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                ban.add(fronts[i])
        tmp = sorted(fronts + backs)

        for num in tmp:
            if num not in ban:
                return num

        return 0


fronts = [1, 2, 4, 4, 7]
backs = [1, 3, 4, 1, 3]
print(Solution().flipgame(fronts, backs))
