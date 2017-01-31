# Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.

def filter_long_words(arg, n):
    print 'arg ', arg
    ans = []
    for word in arg:
        print 'word ', word
        if len(word) > n:
            ans.append(word)
    print 'ans ', ans
    return ans

filter_long_words(['one', 'two', 'three', 'four', 'five'], 3)
