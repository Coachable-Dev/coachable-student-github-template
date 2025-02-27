class MedianFinder(object):

    def __init__(self):
        #Max heap for lower half
        self.hi = []
        #Min heap for upper half
        self.lo = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        #Add to max heap by default
        heappush(self.lo, -num)

        #Balance heaps if needed.
        #1. Move largest from lower half to upper half
        heappush(self.hi, -heappop(self.lo))

        #2. If size difference greater than 1, move one back
        if len(self.lo) < len(self.hi):
            heappush(self.lo, -heappop(self.hi))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.lo) > len(self.hi):
            #odd number of elements
            return float(-self.lo[0])
        #Even number of elements
        return ((-self.lo[0] + self.hi[0]) / 2.0)

        #time O(log n) addNum O(1) findMedian
        #space O(1)
