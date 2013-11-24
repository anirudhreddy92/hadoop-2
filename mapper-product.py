# Your task is to make sure that this mapper code does not fail on corrupt data lines,
# but instead just ignores them and continues working
import sys

def mapper(datainput):
	# read standard input line by line
	print "Mapper executed" 
	
	count = 0
	while count < 10:
		print datainput[count]
		count += count
	
	for line in datainput:
		# strip off extra whitespace, split on tab and put the data in an array
		#print line
		data = line.strip().split("\t")

		# This is the place you need to do some defensive programming
		# what if there are not exactly 6 fields in that line?
		if len(data) == 6:

		# this next line is called 'multiple assignment' in Python
		# this is not really necessary, we could access the data
		# with data[2] and data[5], but we do this for conveniency
		# and to make the code easier to read
			date, time, store, item, cost, payment = data

		# Now print out the data that will be passed to the reducer
			#print "{0}\t{1}".format(item, cost)

test_text = """2013-10-09\t13:22\tMiami\tBoots\t99.95\tVisa
2013-10-09\t13:22\tNew York\tDVD\t9.50\tMasterCard
2013-10-09 13:22:59 I/O Error
^d8x28orz28zoijzu1z1zp1OHH3du3ixwcz114<f
1\t2\t3"""

# This function allows you to test the mapper with the provided test string
def main():
	import StringIO
	print sys.argv[1]
	#salesdata = sys.argv[1:]
	datafile = open(sys.argv[1], 'r')
	#for arg in argv:
		#salesdata = arg
	mapper(datafile)
	#sys.stdin = sys.__stdin__

main()