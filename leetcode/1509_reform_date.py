"""1509. Reform Date"""
class Solution:
    """Solution Class"""
    def reformatDate(self, date: str) -> str:
        """
        #This function converts a date in the format 'Day Month Year' into the format 'YYYY-MM-DD'.
        #It handles converting the day to two digits, mapping month names to numeric values, 
        #and reconstructing the formatted string.
        #Loom Explanation: https://www.loom.com/share/d57df9ca5f174c35be7be5b00e3c4f29
        """
        #First we need to split our given date
        splits = date.split(" ")
        #We then proceed by grabbign our first value (Day)
        #It is important to ensure that we are extracitng the numerical date out of the
        #input given original day.
        dd = splits[0][0:len(splits[0])-2]
        #We will proceed by mapping each month to its respective numeric equivalent
        month = {"Jan":"01", "Feb":"02", "Mar": "03", "Apr":"04",
        "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09",
        "Oct":"10","Nov":"11",'Dec':"12"}
        #We will be checking if the day is a one digit or 2 digits.
        #If 2 digits then we will leave as it is, meanwhile if it's 1 digit
        #We will be adding an additional starting '0'
        if(int(dd)//10) == 0:
            dd = str('0') + str(dd)
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        return splits[2] + "-" + month[splits[1]] + "-" + str(dd)
