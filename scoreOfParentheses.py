class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        def sub(a):
            if a == '()':
                return 1
            stack = []

            for i in range(len(a)):
                if a[i] == '(':
                    stack.append('(')
                else:
                    stack.pop()

                    if len(stack) == 0 and i != len(a) - 1:
                        return sub(a[:i + 1]) + sub(a[i + 1:])

            return 2 * sub(a[1:len(a) - 1])

        return sub(s)


s = "()"
s = "(())"
s = "()()"
s = "(()(()))"
print(Solution().scoreOfParentheses(s))
