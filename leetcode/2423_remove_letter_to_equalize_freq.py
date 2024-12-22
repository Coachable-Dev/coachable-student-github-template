"""2423. Remove Letter To Equalize Frequency"""

class Solution:
    """Solution Class"""
    def equalFrequency(self, word: str) -> bool:
        """
        This function determines if removing one character can make the frequency 
        of all other characters equal. It uses two hashmaps: one to count occurrences 
        of each character and another to track frequency counts.
        #Loom: https://www.loom.com/share/
        #7437e32fbfb34816aad0d5b850e9e8c5?sid=7b0fe657-a357-4891-989c-eadbb56c5e2a
        """
        #We will start by counting the occurrences of each char
        counting = {}
        #We will be storing the frequencies in this other hashmap
        freqs = {}
        #Time Complexity: O(n)
        for chr in word:
            if chr in counting:
                counting[chr] +=1
            else:
                counting[chr] = 1
        #Time Complexity: O(n)
        for fr in counting.values():
            if fr in freqs:
                freqs[fr] += 1
            else:
                freqs[fr] = 1
        #Overall Time Complexity: O(n) + O(n) = O(n)
        #Space Complexity O(n)
        #If len of freqs == 1
        if len(freqs)==1:
            return 1 in freqs or 1 in freqs.values()
        if len(freqs) ==2:
            #We need to obtain both the largest and min value from our freqs
            f1 = min(freqs.keys())
            f2 = max(freqs.keys())
            return (f1 + 1 == f2 and freqs[f2] == 1) or (f1 == 1 and freqs[f1] == 1)
        return False
