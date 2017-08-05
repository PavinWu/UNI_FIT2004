#def decompress(bwt):	# O(2N + M) = O(N)	assuming M = 256 = const OR O(M) if M>N
def main_decode(bwt):
	# bwtSorted = bwt.split('').sort().join()	# don't even need this since we never access 1st col
	charNum, occurence = createNum(bwt)
	rank = createRank(occurence)
	
	row = 0
	str = ''
	for _ in range(len(bwt)):
		c = bwt[row]
		str = c + str
		row = rank[ord(c)] + charNum[row] - 1
	return str[1:]	# 0th char of str is '$'
		
def createNum(bwt):	# O(N)
	occurence = [0]*256	# assume M = 256 = const
	charNum = []	# occurence of chars in last col 
	for i in range(len(bwt)):
		char = bwt[i]
		codePoint = ord(char)
		occurence[codePoint] += 1
		charNum.append(occurence[codePoint])
	return charNum, occurence
		
# we can create rank array without having to sort because occurence is already sorted.
# we know occurence is sorted becasue we allocate its index based on (value we can retrive from) ord() function
#	i.e. we store data on array which allow direct accessing with indices in sorted order.
#	i.e. we had sorted structure in the first place: no need to explicitly sort
# assume ord function can retrive the unicode of a character in O(1). 
def createRank(occurence):	# O(M)
	rank = [-1]*256	# assume M = 256 = const
	i = 0
	Index1stCol = 0	# Index in 1st col for next char 
	for i in range(len(occurence)):
		if occurence[i] != 0:
			rank[i] = Index1stCol
			Index1stCol = rank[i] + occurence[i]
	return rank
			
	"""
	prevChar = bwtSorted[0]
	count = 0
	for char in bwtSorted:	# create rank array
		if char == prevChar:
			count += 1
		else:
			rank.append([prevChar, count])
			prevChar = char
			count = 1
	rank.append([prevChar, count])
	return rank
	"""
	
if __name__ == "__main__":
	#f = open('test.txt', 'r')
	#f = open('test2_out.bz2', 'r')
	f = open('exam.bz2', 'r')
	bwt = ""
	for line in f:
		line = line.split()
		for i in range(int(line[0])):	# skip last (i.e. last num on right)! (if want to run *once*, need to end with 1!)
			bwt = bwt + line[1]
	origText = main_decode(bwt)
	origText = origText.replace('-', '\n')
	origText = origText.replace('*', ' ')
	print(origText)
	# damn ...