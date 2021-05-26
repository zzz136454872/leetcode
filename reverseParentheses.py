class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for letter in s:
            if letter != ')':
                stack.append(letter)
            else:
                j = len(stack) - 1

                while stack[j] != '(':
                    j -= 1
                stack = stack[:j] + stack[len(stack) - 1:j:-1]

        return ''.join(stack)


sl = Solution()
s = "(abcd)"
s = "(ed(et(oc))el)"
s = "a(bcdefghijkl(mno)p)q"
print(sl.reverseParentheses(s))
