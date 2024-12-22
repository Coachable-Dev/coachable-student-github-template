"""57. Insert Interval"""
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        """
        # This function inserts a new interval into a list of sorted, non-overlapping intervals
        #and merges any overlapping intervals to ensure that the resulting intervals remain
        #sorted and non-overlapping.
        #Loom: https://www.loom.com/share/
        #49b3a7e8faf14012b274297443082570?sid=febff73b-da83-4333-b3e6-32789ee123a3
        """
        #We will start by declaring an empty array that we will use to store the result
        result = []
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        #We want to iterate over the range of intervals and check whether
        #First I'll be checkign that newInterval[1] is smaller than the start of my first interval
        for i,interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                result.append(newInterval)
                return result + intervals[i:]

            if newInterval[0] > interval[1]:
                result.append(interval)
            #We also have to merge the overlapping interval/newInterval
            else:
                newInterval = (min(intervals[i][0], newInterval[0]),
                               max(intervals[i][1], newInterval[1]))
        result.append(newInterval)
        return result
