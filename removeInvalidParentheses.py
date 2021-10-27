from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def valid(s):
            balance = 0

            for letter in s:
                if letter == '(':
                    balance += 1
                elif letter == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        left = 0
        right = 0

        for letter in s:
            if letter == '(':
                left += 1
            elif letter == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1

        out = []

        def search(substring, start, lcount, rcount, lremove, rremove):
            print(substring, start, lcount, rcount, lremove, rremove)

            if lremove == 0 and rremove == 0:
                if valid(substring):
                    out.append(substring)

                return

            for i in range(start, len(substring)):
                if i != start and substring[i] == substring[i - 1]:
                    if substring[i] == ')':
                        rcount += 1
                    elif substring[i] == '(':
                        lcount += 1

                    if rcount > lcount:
                        return

                    continue

                if lremove + rremove > len(substring) - i:
                    return

                if lremove > 0 and substring[i] == '(':
                    # print('left',lremove, i, substring[:i-1]+substring[i+1:])
                    search(substring[:i] + substring[i + 1:], 0, 0, 0,
                           lremove - 1, rremove)

                if rremove > 0 and substring[i] == ')':
                    # print('right',rremove, i, substring[:i-1]+substring[i+1:])
                    search(substring[:i] + substring[i + 1:], 0, 0, 0, lremove,
                           rremove - 1)

                if substring[i] == ')':
                    rcount += 1
                elif substring[i] == '(':
                    lcount += 1

                if rcount > lcount:
                    return

        search(s, 0, 0, 0, left, right)
        print(out)

        return list(set(out))


s = "()())()"
s = "(a)())()"
s = ")("
s = ")(()c))("
# s='(()c)('
print(Solution().removeInvalidParentheses(s))
