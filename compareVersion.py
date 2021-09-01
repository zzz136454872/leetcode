class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        i = 0
        m = min(len(v1), len(v2))

        for i in range(m):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1

        for i in range(m, len(v1)):
            if v1[i] > 0:
                return 1

        for i in range(m, len(v2)):
            if v2[i] > 0:
                return -1

        return 0


sl = Solution()
version1 = "1.01"
version2 = "1.001"
version1 = "1.0"
version2 = "1.0.0"
version1 = "0.1"
version2 = "1.1"
version1 = "1.0.1"
version2 = "1"
version1 = "7.5.2.4"
version2 = "7.5.3"
print(sl.compareVersion(version1, version2))
