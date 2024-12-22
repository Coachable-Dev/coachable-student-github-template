"""1122. Relative Sort Array"""
class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        """
        This function sorts arr1 such that elements in arr2 appear first and in their respective
        order, followed by the rest of the elements from arr1 sorted in ascending order.
        #Loom: https://www.loom.com/share/6b15a791d545442789efae67caf503f6
        """
        count_Array1 = {}
        endArray = []
        result = []
        #Time Complexity
        #Space Complexity O(n)
        #We have to first count how many times each number happens by mapping them to their
        #frequency
        #Time Complexity O(n)
        for num in arr1:
            if num in count_Array1:
                count_Array1[num] += 1
            else:
                count_Array1[num] = 1
        #Now we have to populate our endArray with all the numbers that are not
        #present in our array2 but that are present in our array1
        #Time Complexity O(m)
        for num in arr1:
        #Space Complexity O(m)
            if num not in arr2:
                endArray.append(num)
        #It is also imperative to sort the endArray before we will be merging it to our result
        #array
        endArray.sort()
        #Now that we have obtained both the hashmap of arr1 and the second part of the nums array
        # that don't appear in our arr1 we can now populate our result by adding
        # by each amount of time the numbers that that we have in our count_Arr1 in the arr2 order
        #Time Complexity O(k)
        #Space Complexity O(m)
        for num in arr2:
            for _ in range(count_Array1[num]):
                result.append(num)
        #Time Complexity O(n) + O(m) + O(k) = O(n + m +k)
        #Space Complexity O(n) + O(m) + O(k) = O(n + m +k)
        return result + endArray