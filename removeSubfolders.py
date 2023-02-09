from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        flags = [True for i in range(len(folder))]
        prev = 0

        for i in range(1, len(folder)):
            if folder[i][:len(folder[prev])] == folder[prev] and \
                    folder[i][len(folder[prev])] == '/':
                flags[i] = False
            else:
                prev = i

        return [folder[i] for i in range(len(folder)) if flags[i]]


folder = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
# folder = ["/a","/a/b/c","/a/b/d"]
# folder = ["/a/b/c","/a/b/ca","/a/b/d"]
folder = ["/c", "/d/c/e"]
print(Solution().removeSubfolders(folder))
