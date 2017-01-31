from sys import argv

# script, first, second, third = argv

def max_of_three(first, second, third):
			
	if first >= second and first >= third:
		print "first is greatest", first
		return first

	if second >= first and second >= third:
		print "second is greatest", second
		return second

	if third >= first and third >= second:
		print "third is greatest", third
		return third

	else:
		return first