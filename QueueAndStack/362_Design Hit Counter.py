'''
Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).

Your system should accept a timestamp parameter (in seconds granularity), and you may assume that calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing). Several hits may arrive roughly at the same time.

Implement the HitCounter class:

HitCounter() Initializes the object of the hit counter system.
void hit(int timestamp) Records a hit that happened at timestamp (in seconds). Several hits may happen at the same timestamp.
int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).
'''

#method 1. Using backets. hit(): O(1), getHits(): O(s) where s == 300.  S(s)
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter = [(0, 0)] * 300

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        timestamp -= 1
        index = timestamp % 300
        if self.counter[index][0] == timestamp:
            self.counter[index] = (timestamp, self.counter[index][1] + 1)
        else:
            self.counter[index] = (timestamp, 1)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        res = 0
        timestamp -= 1
        for i in range(300):
            if timestamp - self.counter[i][0] < 300:
                res += self.counter[i][1]
        return res

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
