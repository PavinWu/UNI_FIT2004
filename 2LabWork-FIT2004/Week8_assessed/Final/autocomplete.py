
class trieNode:
	def __init__(self):		# This is how you initiate multiple "attributes" to one thing: OO
		self.pointers = [None]*27	# 27 for $. Assume only small English alphabets are used
		self.max_cNode = 0			# max child node to go to
		self.max_cNode_freq = 0
		self.descp = None		# only the last node (with '$') has the descp
		self.num_cNode = 0			# number of child nodes	#WORNG(one level down only)
		
		
class trie:
	def __init__(self):
		self.root = trieNode()
		
	def insertWord(self, word, freq, descp):
		current = self.root		# current root will always be of previous character
		for i in range(len(word)):
			letter_index = ord(word[i]) - 97
			
			if current.pointers[letter_index] is None:		# if no letter, first create a child node at the letter
				current.pointers[letter_index] = trieNode()		# this also records presence of this letter
			# a new node is created regardless of whether this new character is max
			# but info about the max node will be updated below if it is max
			
			# to determine if alphabetically smaller. Just need to compare the current letter!
			if current.max_cNode_freq < freq or (current.max_cNode_freq == freq and letter_index < current.max_cNode):			
			# if freq of new word > max freq of present child nodes OR they are equal but new word is shorter
				# become the new max cNode (trial of max word)
				current.max_cNode = letter_index			# update new max child node
				current.max_cNode_freq = freq		

			current.num_cNode += 1	## mistake (you put it below the line below)
			current = current.pointers[letter_index]	 # tread along the node (for the current word, regardless of whether it is max) 
			
			if i == len(word) - 1:	# if last letter
				current.pointers[26] = '$'	 # last position to store $	   
				current.max_cNode = 26
				current.max_cNode_freq = freq
				current.descp = descp		 # description of *This* word. Only at last node with '$'
				current.num_cNode += 1		## mistake (wasn't here)
				
	def suggestWord(self, prefix):
		current = self.root
		suggested_word = prefix
		
		# go through trie through characters in prefix
		for i in range(len(prefix)):
			s_letter_index = ord(prefix[i]) - 97
			try:
				if current.pointers[s_letter_index] is None:	# no child node
					return None, 0, None, 0
			except IndexError:	# word length exceed the word with max length in this section of trie
				return None, 0, None, 0
				
			current = current.pointers[s_letter_index]
				
		# go through trie to extract best word. 
		reachBestWord = False		# if reach the word with max freq
		i = 0
		num_cNode = current.num_cNode
		while not reachBestWord:		
			if current.max_cNode == 26:
				reachBestWord = True
				return suggested_word, current.max_cNode_freq, current.descp, num_cNode
			else:
				suggested_word += chr(current.max_cNode + 97)
				current = current.pointers[current.max_cNode]	# go to max child node
			
			# note: nodes below will never have freq greater than parent. In fact, they are same. [Node with a freq Need to go through parent first]
				# thus: we can always just look at the node with greatest freq, and it will guarantee to be a valid word
	
if __name__ == "__main__":
	trie_words = trie()
	
	f = open('Dictionary.txt', 'r')
	i = 0
	for line in f:
		if line != '\n':		   # if not empty line	
			if i == 0:
				word = line[6:].rstrip()	# don't take 'word: ', then strip off '/n'
				i += 1
			elif i == 1:
				frequency = int(line[11:].rstrip())
				i += 1
			elif i == 2:
				description = line[12:].rstrip()
				i = 0
				trie_words.insertWord(word, frequency, description)
	
	prefix = ''
	while prefix != '***':
		prefix = input('Enter prefix: ')
		if prefix != '***':
			suggested_result = trie_words.suggestWord(prefix)	# word, freq, descp, num_cNode
			if suggested_result[0] is not None:	
				print('Auto-complete suggestion: ' + suggested_result[0])
				print('Definition: ' + suggested_result[2])
				print(str(suggested_result[3]) + ' word(s) in the dictionary which has "' + prefix + '" as a prefix')
			else:
				print('There is no word in the dictionary which has "' + prefix + '" as a prefix')

		
	  
	