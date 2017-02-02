# Write a function char_freq() that takes a string and builds a frequency listing of the characters contained in it. Represent the frequency listing as a Python dictionary. Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").


def char_freq(arg):
    count = dict()
    test = list(arg)
    for char in test:
        try:
            count[char] += 1
        except KeyError:
            count[char] = 1
    return count

print 'anser is ', char_freq(',;,;./?.,')