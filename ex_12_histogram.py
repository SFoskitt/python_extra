# Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:

# ****
# *********
# *******

# Uncomment the following to get output in the terminal (run as 'python ex_12_histogram.py')
# def histogram(lst):
#     length = len(lst)
#     ans = ''
#     for i in range(0,length,1):
#         print '*!' * lst[i]
#         ans += '*' * lst[i] + '\n'
    
#     print 'ans', ans
#     return ans
# list_arg = map(int, raw_input('List of numbers: ').split(','))
# histogram(list_arg)


# The following is the same logic but setup to test
def histogram(lst):
    length = len(lst)
    ans = ''
    for i in range(0,length,1):
        ans += '*' * lst[i] + '\n'
    
    return ans
