from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        mem = [[-1] * len(piles) for i in range(len(piles))]

        def advantage(sp, ep):
            if ep < sp:
                return 0

            if mem[sp][ep] != -1:
                return mem[sp][ep]
            tmp = max(piles[sp] + advantage(sp + 1, ep),
                      piles[ep] + advantage(sp, ep - 1))
            mem[sp][ep] = tmp

            return tmp

        return advantage(0, len(piles) - 1) > 0


sl = Solution()
piles = [5, 3, 4, 5]
print(sl.stoneGame(piles))
