# A pangram is a sentence that contains all the letters of the English alphabet at least once, for example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to see if it is a pangram or not.

def panagram(arg):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for letter in arg:
        if letter in alphabet:
            alphabet.remove(letter)
    
    if len(alphabet) == 0:
        return True
    else:
        return False

# thing = 'the quick brown fox jumps over the lazy dog'
# print 'pass is ', thing, ' a panagram ', panagram(thing)