class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        out = 0

        for i in range(31):
            mask = 1 << i

            if (x & mask) ^ (y & mask):
                out += 1

        return out


sl = Solution()
x = 1
y = 4
print(sl.hammingDistance(x, y))
