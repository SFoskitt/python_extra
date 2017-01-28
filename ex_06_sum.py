
def sum():
    s = raw_input('enter space-delimited list of numbers ')
    sum_list = map(int, s.split())
    ans = 0
    for number in sum_list:
        print 'the next number is sum_list', number
        ans += number
    print 'the sum ans is ', ans
    return ans

def multiply():
    s = raw_input('enter space-delimited list of numbers ')
    mult_list = map(int, s.split())
    ans = 1
    for number in mult_list:
        ans = ans * number
    print 'the mult ans is ', ans
    return ans

sum()
multiply()