from typing import *

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        log={}
        for s in strs:
            key=''.join(sorted(list(s)))
            if key not in log.keys():
                log[key]=[s]
            else:
                log[key].append(s)
        return list(log.values())

inp=["eat", "tea", "tan", "ate", "nat", "bat"]
sl=Solution()
print(sl.groupAnagrams(inp))
