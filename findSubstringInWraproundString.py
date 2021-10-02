class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        def isNext(a, b):
            if ord(b) == ord(a) + 1:
                return True

            if a == 'z' and b == 'a':
                return True

            return False

        mem = {chr(i + ord('a')): 0 for i in range(26)}
        length = 1
        mem[p[0]] = 1

        for i in range(1, len(p)):
            if isNext(p[i - 1], p[i]):
                length += 1
            else:
                length = 1
            mem[p[i]] = max(mem[p[i]], length)

        return sum(mem.values())


p = "a"
# p="cac"
# p="zab"
print(Solution().findSubstringInWraproundString(p))
