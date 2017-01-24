#Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise, you should (also) write it using two nested for-loops.

def overlapping(list1, list2):
    length1 = len(list1)
    length2 = len(list2)

    for item in list1:
        if item in list2:
            return True
    
    return False

ans = overlapping(raw_input('Enter list 1:  '), raw_input('Enter list 2:  '))
print "The answer is ", ans