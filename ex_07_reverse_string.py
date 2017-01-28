str = raw_input('enter a string ')
length = len(str)
ans = ''
for i in range(length-1,-1,-1):
    ans += str[i]
print 'string reversed ', ans
