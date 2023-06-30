class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        ss = sentence.split()

        for i in range(len(ss) - 1):
            if ss[i][-1] != ss[i + 1][0]:
                return False

        if ss[0][0] != ss[-1][-1]:
            return False

        return True


sentence = "leetcode exercises sound delightful"
sentence = "eetcode"
sentence = "Leetcode is cool"
print(Solution().isCircularSentence(sentence))
