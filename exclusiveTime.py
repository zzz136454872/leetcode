from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        START = 0
        END = 1

        def parse(s):
            a = s.find(':')
            p = int(s[:a])
            b = s.find(':', a + 1)

            if b - a == 6:
                op = START
            else:
                op = END
            t = int(s[b + 1:])

            return (p, op, t)

        res = [0] * n
        stack = []
        last = 0

        for log in logs:
            p, op, t = parse(log)

            if op == START:
                if len(stack) > 0:
                    res[stack[-1]] += t - last
                stack.append(p)
                last = t
            else:
                stack.pop()
                res[p] += t - last + 1
                last = t + 1

        return res


n = 2
logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
n = 1
logs = ["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"]

n = 2
logs = ["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"]
n = 2
logs = ["0:start:0", "0:start:2", "0:end:5", "1:start:7", "1:end:7", "0:end:8"]
n = 1
logs = ["0:start:0", "0:end:0"]

print(Solution().exclusiveTime(n, logs))
