
def is_vowel(test):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return test.lower() in vowels

def modify_string():
    candidate = raw_input('get a string')
    ans = ''
    for letter in candidate:
        if is_vowel(letter):
            #do something
            ans += letter
            print ans
        else:
            #do something else
            ans += letter + 'o' + letter
            print ans
    
    print 'completed string', ans
    return ans

modify_string()