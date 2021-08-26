from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i = 0
        j = len(people) - 1
        people.sort()
        out = 0

        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            out += 1

        return out


sl = Solution()
people = [1, 2]
limit = 3
people = [3, 2, 2, 1]
limit = 3
people = [3, 5, 3, 4]
limit = 5
print(sl.numRescueBoats(people, limit))
