"""1768. Merge Strings Alternately"""
class Solution:
    """Solution Class"""
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        #This function merges two strings alternately, appending characters 
        #from word1 and word2 one by one. If one string is longer, the 
        #remaining characters are appended at the end.
        #Loom explanation:
        #https://www.loom.com/share/
        #b5fa34deb0ad435bbee2ed6879ca43e7?sid=2b1f2195-e382-4431-af47-f37d9e1e2de8
        """
        # Time Complexity: O(m + n)
        # Reasoning: We iterate through both word1 and word2 once, appending
        # their characters to the result list.
        # m = length of word1, n = length of word2
        # Space Complexity: O(m + n)
        # Reasoning: The result list stores the combined characters of word1 and word2,
        # requiring O(m + n) space.
        # Step 1: Initialize two pointers for word1 and word2.
        i,j = 0,0
        # Step 2: Initialize the result list to store characters alternately.
        result = []
        #We will be using an iterative while loop which will run
        #according to the condition that i<len(word1) and j<len(word2)
        #We will be using these two pointers to point to each char individually
        #So we can insert/append to our result array each character alernately
        while i<len(word1) and j<len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i+=1
            j+=1
        #It could be the case that either word1 or word2 still have some characters
        #that needs to be appended to our reuslt.
        # So we will be keep adding any leftovers chars
        #Adding any remaining chars from word1 (if there are any)
        if i<len(word1):
            result.append(word1[i:])
        #Adding any remaining chars from word2 (if there are any)
        if j<len(word2):
            result.append(word2[j:])
        #To convert our array into a string.
        result = "".join(result)
        return result
