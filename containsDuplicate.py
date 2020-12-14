from typing import *

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        table={}
        for num in nums:
            if num in table.keys():
                return True
            else:
                table[num]=1
        return False
