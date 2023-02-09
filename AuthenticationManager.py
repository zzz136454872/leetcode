from typing import *


def kLargest(nums, k):
    """返回nums中第k大的数，从1开始计数"""
    pass


class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.mem = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.mem[tokenId] = currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.mem.keys():
            return
        diedTime = self.mem[tokenId]

        if diedTime > currentTime:
            self.mem[tokenId] = currentTime + self.ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        out = 0
        del_list = []

        for t, v in self.mem.items():
            if v <= currentTime:
                del_list.append(t)
            else:
                out += 1

        for t in del_list:
            del self.mem[t]

        return out


timeToLive = 5

authenticationManager = AuthenticationManager(5)
authenticationManager.renew("aaa", 1)
authenticationManager.generate("aaa", 2)
print(authenticationManager.countUnexpiredTokens(6))
authenticationManager.generate("bbb", 7)
authenticationManager.renew("aaa", 8)
authenticationManager.renew("bbb", 10)
print(authenticationManager.countUnexpiredTokens(15))
