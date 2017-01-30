#The function max() from exercise 1) and the function max_of_three() from exercise 2) will only work for two and three numbers, respectively. But suppose we have a much larger number of numbers, or suppose we cannot tell in advance how many they are? Write a function max_in_list() that takes a list of numbers and returns the largest one.

# Uncomment the following to run in terminal (python ex_13_max_in_list.py)

# def max_in_list(list_arg):
#     ans = list_arg[0]
#     for i in list_arg:
#         if i > ans:
#             ans = i
#     return ans

# arg = map(int, raw_input('Numbers by commas: ').split(','))
# end = max_in_list(arg)
# print 'Answer is ', end


# The following here is the same logic set up for testing

def max_in_list(list_arg):
    if len(list_arg):
        ans = list_arg[0]
        for i in list_arg:
            if i > ans:
                ans = i
        return ans
    else:
        return None