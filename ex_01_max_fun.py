from sys import argv

script, first, second = argv

def max(first, second):

	if first > second:
			print "first is greater", first
			return first
	else:
		print "second is greater", second
		return second

# print "the answer is ", max(first, second)