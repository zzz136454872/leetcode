class Solution:
    def secondHighest(self, s: str) -> int:
        nums = set()

        for l in s:
            if l.isdigit():
                nums.add(int(l))
        nums = list(nums)
        nums.sort(reverse=True)

        if len(nums) > 1:
            return nums[1]

        return -1


sl = Solution()
inp = "dfa11111"
print(sl.secondHighest(inp))
