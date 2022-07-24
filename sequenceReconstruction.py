from typing import List


class Solution:
    def sequenceReconstruction(self, nums: List[int],
                               sequences: List[List[int]]) -> bool:
        n = len(nums)
        mem = [[] for i in range(n + 1)]
        front = [0] * (n + 1)

        for sequence in sequences:
            for i in range(len(sequence) - 1):
                mem[sequence[i]].append(sequence[i + 1])
                front[sequence[i + 1]] += 1

        queue = []

        for i in range(1, n + 1):
            if front[i] == 0:
                queue.append(i)

        while len(queue) > 0:
            if len(queue) > 1:
                return False
            now = queue.pop()

            for nxt in mem[now]:
                front[nxt] -= 1

                if front[nxt] == 0:
                    queue.append(nxt)

        return True


nums = [1, 2, 3]
sequences = [[1, 2], [1, 3]]
nums = [1, 2, 3]
sequences = [[1, 2]]
nums = [1, 2, 3]
sequences = [[1, 2], [1, 3], [2, 3]]
print(Solution().sequenceReconstruction(nums, sequences))
