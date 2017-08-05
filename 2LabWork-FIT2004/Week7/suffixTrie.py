class trieNode:
	"""
	Assume only English small alphabets
	"""
	def __init__(self):
		self.letters = [None]*27
		self.occurrence = 0

class trie:
	"""
	Assume only English small alphabets
	"""
	def __init__(self):
		self.root = trieNode()

	def generateSuffixTrie(self, str):
		for i in range(len(str)):
			current = self.root
			for j in range(i, len(str)):
				letter_index = ord(str[j]) - 97
				if current.letters[letter_index] is None:
					current.letters[letter_index] = trieNode()
				# self.occurrence += 1	# trie not have this attribute, but trie.root (trieNode) does.
				current.occurrence += 1
				current = current.letters[letter_index]
				if j == (len(str) - 1):
					current.occurrence += 1		
					current.letters[26] = '$'
	
	def isSubString(self, sub):
		current = self.root
		for i in range(len(sub)):
			letter_index = ord(sub[i]) - 97
			if current.letters[letter_index] is None:
				return False
			current = current.letters[letter_index]
		return True	
	
	def countOccurrence(self, sub):	# count how many $ there are in the node of suffix sub
		current = self.root
		for i in range(len(sub)):
			letter_index = ord(sub[i]) - 97
			if current.letters[letter_index] is None:
				return 0
			current = current.letters[letter_index]
		return current.occurrence
	
	def longestRepeatedSub(self):
		
	
if __name__ == "__main__":
	str = 'mississippi'
	aTrie = trie()
	aTrie.generateSuffixTrie(str)
	print(aTrie.isSubString('missis'))
	print(aTrie.isSubString('sisdf'))
	print(aTrie.countOccurrence('p'))
	