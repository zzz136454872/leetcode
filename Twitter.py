
from typing import *

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.log=[]
        self.f={}

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.log.append((userId,tweetId))

        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId in self.f.keys():
            ids=self.f[userId]
        else:
            ids=[]
        ids.append(userId)
        count=0
        out=[]
        
        for news in self.log[::-1]:
            if news[0] in ids:
                count+=1
                out.append(news[1])
                if count>=10:
                    break
        return out

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.f.keys():
            if f not in self.f[followerId]:
                self.f[followerId].append(followeeId)
        else:
            self.f[followerId]=[followeeId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.f.keys() and followeeId in self.f[followerId]:
            self.f[followerId].remove(followeeId)

twitter = Twitter();
twitter.postTweet(1, 5)
print(twitter.getNewsFeed(1))
print(type(twitter))
twitter.follow(1, 2)
twitter.postTweet(2, 6)
print(twitter.getNewsFeed(1))
twitter.unfollow(1, 2)
twitter.getNewsFeed(1)
