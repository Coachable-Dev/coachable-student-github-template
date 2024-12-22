"""986. Interval List Intersections"""
class Solution:
    def intervalIntersection(self, firstList: list[list[int]],
                            secondList: list[list[int]]) -> list[list[int]]:
        """
        #This function computes the intersection of two lists of intervals.
        #Loom: https://www.loom.com/share/1586f6f15bde4570acceaeb9f3267d83
        """
        #I'll initialize two pointers
        p1,p2 = 0,0
        #Here I'll delcare my result array where I'll be appending any overlaps
        result = []
        #Time Complexity O(n + m)
        #Space Complexity O(n)
        if (len(firstList) == 0 or len(secondList) == 0):
            return []
        #To start iterating using a while loop untill p1< len(firstList) or p2< len(secondList)
        while (p1<len(firstList) and p2<len(secondList)):
            start1, end1 = firstList[p1]
            start2, end2= secondList[p2]
            if start1 > end2:
                p2 += 1
            elif start2 > end1:
                p1 +=1
            else:
                result.append([max(start1,start2), min(end1,end2)])
                if end1 > end2:
                    p2+=1
                else:
                    p1 +=1
        return result
