class Solution:
    def simplifyPath(self, path: str) -> str:
        tmp = []
        path = path.split('/')

        for p in path:
            if p == '' or p == '.':
                continue

            if p == '..':
                if len(tmp) > 0:
                    tmp.pop()

                continue
            tmp.append(p)
        out = ''

        for p in tmp:
            out += '/' + p

        if len(out) == 0:
            return '/'

        return out


path = "/home/"
path = "/../"
path = "/home//foo/"
path = "/a/./b/../../c/"
print(Solution().simplifyPath(path))
