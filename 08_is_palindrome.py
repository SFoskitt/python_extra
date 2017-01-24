def palindrome_test(str):
    length = len(str)
    backwards = ''

    for i in range(length-1,-1,-1):
        backwards += str[i]

    print 'string reversed ', backwards

    if str == backwards:
        return True
    else:
        return False

print palindrome_test(raw_input('Enter a string:  '))
