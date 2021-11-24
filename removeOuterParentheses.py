class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        queue = []
        pre = 0

        for i in range(len(s)):
            # print(i,stack,queue)

            if s[i] == '(':
                stack.append(s[i])

                continue
            stack.pop()

            if len(stack) == 0:
                queue.append(s[pre:i + 1])
                pre = i + 1
        out = ''

        for p in queue:
            out += p[1:len(p) - 1]

        return out


s = "(()())(())"
s = "(()())(())(()(()))"
print(Solution().removeOuterParentheses(s))
