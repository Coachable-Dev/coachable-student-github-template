'''973. K Closest Points to Origin'''
import heapq
from typing import List

class Solution:
    '''Solution Class'''
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        Iterates through the points and finds the distances of the points
        and adds them to a heap by distance to sort them and then returns
        the k points that are closest to the origin (0,0) by return the 
        the k smallest points from the heap.
        Runtime: O(nlogn) -> n from iterating over the points and logn 
                             for adding a value to the heap
        Space: O(n) -> the heap
        '''
        dists = []
        for point in points:
            d = point[0]*point[0] + point[1]*point[1]
            heapq.heappush(dists, (d,point))
        return [p for d, p in heapq.nsmallest(k, dists)]
