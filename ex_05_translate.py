
def is_vowel(test):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return test.lower() in vowels

def modify_string(candidate):
    # candidate = raw_input('get a string')
    ans = ''
    for letter in candidate:
        if is_vowel(letter):
            ans += letter
            print ans
        else:
            ans += letter + 'o' + letter
            print ans
    
    print 'completed string', ans
    return ans

# modify_string()