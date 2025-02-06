'''921. Minimum Add to Make Parentheses Valid'''
class Solution:
    '''Solution Class'''
    def minAddToMakeValid(self, s: str) -> int:
        '''
        Iterates over the string and with a stack, adds 1 to it if the 
        current character is a '('. If the current character is a ')' and 
        the stack isn't 0, we subtract 1 from the stack. Else, we add on to
        the total as it is a ')' with out a matching '('. The at the end we
        return the total along with the stack as the number in the stack 
        represents any leftover '(' in the string.
        Runtime: O(n) -> to iterate over the string
        Space: O(1) -> the stack is represent by an integer value
        '''
        stack, total = 0, 0
        for paren in s:
            if paren == '(':
                stack += 1
            elif stack:
                stack -= 1
            else:
                total += 1
        return total + stack
          