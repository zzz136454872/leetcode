class Solution:
    def digitCount(self, num: str) -> bool:
        return all([
            True if int(num[i]) == num.count(str(i)) else False
            for i in range(len(num))
        ])


num = "030"
num = "1210"
print(Solution().digitCount(num))
