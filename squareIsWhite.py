class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return (ord(coordinates[0])+ord(coordinates[1]))%2!=0

coordinates = "a1"
print(Solution().squareIsWhite(coordinates))
