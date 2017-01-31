# Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually ignored.

def clean_string(phrase):
    punct = [' ', ',', '.', ';', ':', '!', '"', "'"]
    ans = ''
    for letter in phrase:
        if letter not in punct:
            ans += letter.lower()
    return ans

def more_pali(phrase):
    phrase_cleaned = clean_string(phrase)
    backwards = ''

    # for i in range(len(phrase)-1,-1,-1):
    for letter in phrase_cleaned:
        backwards += letter
    
    # print 'phrase ', phrase
    # print 'phrase_cleaned ', phrase_cleaned
    # print 'backwards', backwards
    # print 'answer is ', phrase_cleaned == backwards
    if phrase_cleaned == backwards:
        return True

# more_pali("Rise to vote sir")