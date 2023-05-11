class Solution:
    def queryString(self, s: str, n: int) -> bool:
        for i in range(1, n + 1):
            if bin(i)[2:] not in s:
                return False

        return True


s = "0110"
n = 3
print(Solution().queryString(s, n))
