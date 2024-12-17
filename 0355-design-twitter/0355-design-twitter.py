class Twitter:
    def __init__(self):
        self.tweets = defaultdict(list)
        self.follows = defaultdict(list)
        self.time = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId in self.follows.keys():
            temp = self.follows[userId] + [userId]
        else:
            temp = [userId]
        res = []
        for i in temp:
            res = res + self.tweets[i]
        heapq.heapify(res)
        final = []
        while res:
            time, tweetId = heapq.heappop(res)
            final.append(tweetId)
        return final[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.follows[followerId]:
            self.follows[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)