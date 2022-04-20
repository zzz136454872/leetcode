class Solution:
    def lengthLongestPath(self, inp: str) -> int:
        inp = inp.split('\n')
        res = 0
        stack = []

        for f in inp:
            level = f.count('\t')

            while len(stack) > level:
                stack.pop()
            stack.append(f.replace('\t', ''))

            if '.' in f:
                print(stack)
                res = max(res, len('/'.join(stack)))

        return res


input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
print(Solution().lengthLongestPath(input))
