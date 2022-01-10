class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        for i in range(1, min(n // 3 + 2, len(num) - 1)):
            if num[0] == '0' and i > 1:
                break

            for j in range(i + 1, min(n * 2 // 3 + 2, len(num))):
                if num[i] == '0' and j > i + 1:
                    break
                tmp = num[:j]
                n1 = int(num[:i])
                n2 = int(num[i:j])

                while len(tmp) < n:
                    n1, n2 = n2, n1 + n2
                    tmp += str(n2)

                if tmp == num:

                    return True

        return False


inp = "112358"
inp = "199100199"
inp = '123'
# inp='10'
inp = '1023'
inp = '101'
print(Solution().isAdditiveNumber(inp))
