from typing import List


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26


sentence = "thequickbrownfoxjumpsoverthelazydog"
print(Solution().checkIfPangram(sentence))
