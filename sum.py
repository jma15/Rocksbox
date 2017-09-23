import re
import time

# String to test
full_string = '''# Today's weather is 80 degrees.
# Next week's weather will be 60, 40, 50, and 55 degrees for the first four days of the week.
# No rain yesterday!

# Next weekend's weather will be 80 and 110! Wow!
'''
#########################################################################
## Simple regex matching
## Pro: Easier to read and understand
## Con: Longer run time, around 3x longer
#########################################################################

def regex_parse(string):
    ''' Function to parse and sum integer from string.

        Runtime: Worst Case O(n*m)
                n = number of character
                m = number of integer
                We need one loop to split by new line (n)
                We need to loop through the array of string to find all the integer (n)
                    For each value in the loop, we need to sum up these value (m)
                    (Best case no int, so dont need to run)
                    (Worst case all int, need to run n times)

        :param string: String to parse int from
    '''
    # Split the string by new line
    line_split = string.split("\n")
    # Loop through the array to parse the int
    for line in range(0, len(line_split)):
        # Get all the integer in the string
        int_arr = re.findall(r"[0-9.]*[0-9]+", line_split[line])
        line_sum = 0
        # Sum up all the integer in the string
        for i in int_arr:
            line_sum += int(i)
        # print the output
        line_string = "# %s: %s" %(line+1, line_sum)
        print(line_string)

print("#"*50)
print("Regex Function Output:")
start = time.time()
regex_parse(full_string)
end = time.time()
print("Total Runtime: %s" % (end - start))

#########################################################################
## Another function to achieve the same result
## Pro: Only needs to run n time, fast
##      More control to get what you want
## Con: More complex and needs more variable
#########################################################################

def is_int(value):
    '''Function to check if char is an int

       :param value: Char to check if its an integer
       :return: Boolean
    '''
    if value >= '0' and value <='9':
        return True

    return False

def manual_loop(string):
    ''' Function to loop through string and sum all integer in each line

        Runtime: Average Case and Worst Case O(n)

        :param string: String to parse int from
    '''
    line_sum = 0
    last_int = 0
    current_int = ""
    line_counter = 1

    for x in range(0, len(string)):
        # if this is an int
        if(is_int(string[x])):
            # Add this to the string and look for more values
            current_int += string[x]
            # Remember that we found an int and keep searching
            last_int = 1
        # There is no more int
        else:
            # If the last value is int, add to line, skip first case
            if last_int == 0 and current_int!='':
                # sum up all the values
                line_sum += int(current_int)
                # reset the current_int
                current_int = ''

            # This is new line
            if string[x] == '\n':
                # print the sum for the line
                line_string = "# %s: %s" % (line_counter, line_sum)
                print(line_string)
                # reset for next line
                line_sum = 0
                line_counter += 1

            # reset the last_int
            last_int = 0

print("#"*50)
print("Manual Function Output:")
start = time.time()
manual_loop(full_string)
end = time.time()
print("Total Runtime: %s" % (end - start))