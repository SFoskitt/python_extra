#Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise, you should (also) write it using two nested for-loops.

def overlapping(l1, l2):
    list1 = l1.split(',')
    list2 = l2.split(',')

    for item1 in list1:
            if item1 in list2:
                return True
    
    return False

ans = overlapping(raw_input('List one: '), raw_input('List two: '))
print 'Its in there? ', ans