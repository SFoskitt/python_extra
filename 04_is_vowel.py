from sys import argv

script, candidate = argv

def is_vowel(candidate):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return candidate.lower() in vowels

print "the answer is ", is_vowel(candidate)
    

