from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        mem = [0] * 2

        for s in students:
            mem[s] += 1

        for sandwich in sandwiches:
            mem[sandwich] -= 1

            if mem[sandwich] < 0:
                return sum(mem) + 1

        return 0


students = [1, 1, 0, 0]
sandwiches = [0, 1, 0, 1]
students = [1, 1, 1, 0, 0, 1]
sandwiches = [1, 0, 0, 0, 1, 1]
print(Solution().countStudents(students, sandwiches))
