from typing import *

class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort()
        log=[123456 for i in range(T+1)]
        log[0]=0
        for clip in clips:
            for i in range(clip[0]+1,clip[1]+1):
                if i>T:
                    break
                log[i]=min(log[i],log[clip[0]]+1)
        return log[-1] if log[-1]!=123456 else -1

sl=Solution()
clips = [[0,4],[2,8]]
T = 5
print(sl.videoStitching(clips,T))


