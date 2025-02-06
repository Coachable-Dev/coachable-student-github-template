'''986. Interval List Intersections'''
from typing import List

class Solution:
    '''Solution Class'''
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        '''
        We create four varaibles to help keep track of the strarting and 
        end points of fistList and secondList. Then we use logic gates to 
        determine if we move one list up an index or not. Then if there is 
        an overlap we find the max value of the starts of both sections and
        then find the minimum value of the ends of of both sections. The
        one that had the greater value of end stays at that index to
        compare with the next section of the other list which gets
        incremented. The start and end that we found the overlap gets
        appended to the result list, Then when either firstList or
        secondList reaches their end we return the result.
        Runtime: O(n) -> iterating over the lists
        Space: O(n) -> the result list
        '''
        if not firstList or not secondList:
            return []
        result = []
        m, n = len(firstList), len(secondList)
        i, j = 0, 0
        while i < m and j < n:
            start_1, end_1 = firstList[i][0], firstList[i][1]
            start_2, end_2 = secondList[j][0], secondList[j][1]
            if end_1 < start_2:
                i += 1
                continue
            elif end_2 < start_1:
                j += 1
                continue
            overlap = []
            if start_1 >= start_2:
                overlap.append(start_1)
            else:
                overlap.append(start_2)
            if end_1 <= end_2:
                overlap.append(end_1)
                i += 1
            else:
                overlap.append(end_2)
                j += 1
            result.append(overlap)
        return result
