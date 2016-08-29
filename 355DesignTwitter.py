import collections
import itertools
class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = collections.defaultdict(list)
        self.followerRelation = collections.defaultdict(set)
        self.timer = itertools.count(step=-1)

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.tweets[userId].append((next(self.timer),tweetId))

        
    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        self.followerRelation[userId].add(userId)
        userFeed= [t for f in self.followerRelation[userId] for t in self.tweets[f]]
        return [t for c,t in sorted(userFeed,key= lambda x: x[0])][:10]

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId == followerId:
            return
        self.followerRelation[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId == followerId:
            return
        self.followerRelation[followerId].discard(followeeId)
    def debugMe(self):
        print("tweets = " + str(self.tweets))
        print("followerRelation = " + str(self.followerRelation))
        print("------------------------------------------------")

if __name__ == '__main__':
    twitter = Twitter()
    twitter.postTweet(1,5)
    twitter.debugMe()
    twitter.follow(1,2)
    twitter.debugMe()
    twitter.follow(2,1)
    twitter.debugMe()
    print(twitter.getNewsFeed(2))
    print(twitter.getNewsFeed(1))
    twitter.debugMe()
    twitter.postTweet(2,6)
    twitter.debugMe()
    print(twitter.getNewsFeed(1))
    twitter.debugMe()
