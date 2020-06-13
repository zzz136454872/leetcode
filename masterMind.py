from typing import *
class Solution:
    def masterMind(self, solution: str, guess: str) -> List[int]:
        right=0
        solution=list(solution)
        guess=list(guess)
        for i in range(4):
            if solution[i]==guess[i]:
                right+=1
                guess[i]='0'
                solution[i]='1'
        seem=0
        for i in range(4):
            if guess[i] in solution:
                seem+=1
                loc=solution.index(guess[i])
                guess[i]='0'
                solution[loc]=1
        return [right,seem]

sl=Solution()
solution="RGBY"
guess="GGRR"
print(sl.masterMind(solution,guess))
        
