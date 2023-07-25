class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum([stones.count(a) for a in jewels])

