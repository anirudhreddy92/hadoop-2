# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab
# %h %l %u %t \"%r\" %>s %b

import sys, re

def mapper(datainput):

	#print "script start"
	#for line in sys.stdin:
	for line in datainput:
		#data = line.strip().split("\t")
		ip = re.search('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
		filename = re.search('(\"(\S+) (.*?) (\S+)\")', line)
		#filename = re.search('(?<=\s\")(.){4,7}(\w+\/?){0,}([\w\-].?){0,}(?<=\s)', line)
		#filepath = re.search('/(\w+\/?){1,}([\w\-].?){2,}(?=\s)', line)
		if ip and filename:
			print "{0}\t{1}".format(ip.group(0), filename.group(3))

# This function allows you to test the mapper with the provided test string
def main():
	import StringIO
	datafile = open(sys.argv[1], 'r')
	mapper(datafile)

main()