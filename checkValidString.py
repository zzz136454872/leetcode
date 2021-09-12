class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        mem = [[-1] * n for i in range(n)]
        target = {'()', '(*', '**', '*)'}

        def valid(left, right):
            if left > right:
                return True

            if mem[left][right] == 1:
                return True

            if mem[left][right] == 0:
                return False
            out = False

            if left == right and s[left] == '*':
                out = True
            # elif right=left+1 and s[left:right+1] in target:
            #     out=True
            elif s[left] + s[right] in target and valid(left + 1, right - 1):
                out = True

            for i in range(left, right):
                if valid(left, i) and valid(i + 1, right):
                    out = True

                    break

            if out:
                mem[left][right] = 1
            else:
                mem[left][right] = 0

            return out

        return valid(0, n - 1)


s = "()"
s = "(*)"
s = "(*))"
s = '('
print(Solution().checkValidString(s))
