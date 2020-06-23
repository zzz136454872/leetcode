
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]

sl=Solution()
print(sl.addBinary('11','1'))
