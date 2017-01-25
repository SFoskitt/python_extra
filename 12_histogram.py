# Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:

# ****
# *********
# *******

def histogram(list):
    length = len(list)
    for i in range(0,length,1):
        print '*' * list[i]

list_arg = map(int, raw_input('List of numbers: ').split(','))
histogram(list_arg)