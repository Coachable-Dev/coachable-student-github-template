#Loom: https://www.loom.com/share/49b3a7e8faf14012b274297443082570?sid=febff73b-da83-4333-b3e6-32789ee123a3
class Solution:
    def insert(self, intervals: list[List[int]], newInterval: List[int]) -> List[List[int]]:
        #We will start by declaring an empty array that we will use to store the result
        result = []
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        #We want to iterate over the range of intervals and check whether 
        #First I'll be checkign that newInterval[1] is smaller than the start of my first interval
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]

            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            #We also have to merge the overlapping interval/newInterval
            else:
                newInterval = (min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1]))
        result.append(newInterval)
        return result

