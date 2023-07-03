from typing import List


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int],
                      k: int) -> int:
        b = sum(reward2)
        d = [reward1[i] - reward2[i] for i in range(len(reward1))]
        d.sort(reverse=True)

        return b + sum(d[:k])


reward1 = [1, 1, 3, 4]
reward2 = [4, 4, 1, 1]
k = 2
print(Solution().miceAndCheese(reward1, reward2, k))
