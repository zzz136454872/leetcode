from typing import List


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        suits.sort()

        if suits[0] == suits[-1]:
            return "Flush"
        ranks.sort()
        mem = {}

        for r in ranks:
            mem[r] = mem.get(r, 0) + 1
        t = max(mem.values())

        if t >= 3:
            return "Three of a Kind"

        if t == 2:
            return "Pair"

        return "High Card"


ranks = [13, 2, 3, 1, 9]
suits = ["a", "a", "a", "a", "a"]
ranks = [4, 4, 2, 4, 4]
suits = ["d", "a", "a", "b", "c"]
ranks = [1, 10, 2, 12, 9]
suits = ["a", "b", "c", "a", "d"]
print(Solution().bestHand(ranks, suits))
