from typing import List


class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        if len(distance) <= 3:
            return False

        if distance[2] <= distance[0] and distance[1] <= distance[3]:
            return True

        for i in range(4, len(distance)):
            if distance[i - 1] <= distance[i - 3] and\
                    distance[i - 2] <= distance[i]:
                return True

            if distance[i - 1] == distance[i - 3] and\
                    distance[i] + distance[i - 4] >= distance[i - 2]:
                return True

            if i >= 5 and distance[i - 1] <= distance[i - 3] and\
                    distance[i] + distance[i - 4] >= distance[i -2] and\
                    distance[i - 1] + distance[i - 5] >= distance[i - 3] and\
                    distance[i - 2] >= distance[i - 4]:
                return True

        return False


distance = [2, 1, 1, 2]
distance = [1, 2, 3, 4]
distance = [1, 1, 1, 1]
distance = [1, 1, 2, 2, 3, 3, 4, 4, 10, 4, 4, 3, 3, 2, 2, 1, 1]
print(Solution().isSelfCrossing(distance))
