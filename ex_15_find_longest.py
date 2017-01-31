# Write a function find_longest_word() that takes a list of words and returns the length of the longest one.

# First solution, the naive route

def find_longest(words):
    ans = 0
    for word in words:
        print 'word', word, 'length', len(word)
        if ans < len(word):
            ans = len(word)
    print 'ans', ans
    return ans

print 'Find longest', find_longest(['one', 'two', 'three', 'four', 'five'])