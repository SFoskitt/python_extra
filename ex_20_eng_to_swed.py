def eng_to_swed(arg):
    dict = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"yar"}
    test = arg.split(' ')
    ans = ''
    for word in test:
        if word != '' and word != ' ':
            ans += dict[word]
            ans += ' '
    return ans

# passtt = 'happy new year'
# print 'passed to method', eng_to_swed(passtt)