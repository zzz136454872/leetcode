class Solution:
    def canChange(self, start: str, target: str) -> bool:
        def parse(s):
            r = []
            j = 0

            for i in range(len(s)):
                if s[i] == 'L' or s[i] == 'R':
                    r.append(i - j)
                    r.append(s[i])
                    j = i + 1
            r.append(len(s) - j)

            return r

        if len(start) != len(target):
            return False
        start = parse(start)
        target = parse(target)

        if len(start) != len(target):
            return False

        print('start', start)
        print('target', target)

        for i in range(1, len(start), 2):
            if start[i] != target[i]:
                return False

            if start[i] == 'L':
                if start[i - 1] < target[i - 1]:
                    return False
                t = start[i - 1] - target[i - 1]
                start[i + 1] += t
            elif start[i] == 'R':
                if start[i - 1] > target[i - 1]:
                    return False
                t = target[i - 1] - start[i - 1]
                start[i + 1] -= t
        print('start', start)
        print('target', target)

        return True


start = "_L__R__R_"
target = "L______RR"
# start = "R_L_"
# target = "__LR"
# start = "_R"
# target = "R_"
print(Solution().canChange(start, target))
