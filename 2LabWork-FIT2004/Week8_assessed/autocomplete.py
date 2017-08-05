
class trieNode:
	def __init__(self):		# This is how you initiate multiple "attributes" to one thing: OO
		self.pointers = [None]*27	# 27 for $. Can improve?
		self.max_cNode = 0			# max child node to go to
		self.max_cNode_freq = 0
		self.descp = None		# only the last node (with '$') has the descp
		self.num_cNode = 0			# number of child nodes	(one level down only)
		#self.max_cNode_letter = 0		# to determined whether a letter is "alphabetically smaller"
		
		
class trie:
	def __init__(self):
		self.root = trieNode()
		
	def insertWord(self, word, freq, descp):
		"""
		@pre-assumption: no identical words
		insert word into trie
		"""
		current = self.root
		for i in range(len(word)):
			letter_index = ord(word[i]) - 97
			
			if current.pointers[letter_index] is None:		# if no letter, first create a child node at the letter
				current.pointers[letter_index] = trieNode()		# this also records presence of this letter
			# Note: a new (different) letter means new child node in the array pointer of *the current node*
				# i.e. it doesn't mean new array
			# a new node is created regardless of whether this new character is max
			# but info about the max node will be updated below if it is max
			
			# to determine if alphabetically smaller. Just need to compare the current letter!
			
			if current.max_cNode_freq < freq or (current.max_cNode_freq == freq and letter_index < current.max_cNode):			
			# if freq of new word > max freq of present child nodes OR they are equal but new word is shorter
				# become the new max cNode (trial of max word)
				current.max_cNode = letter_index			# update new max child node
				current.max_cNode_freq = freq		
				current.max_cNode_len = len(word)
			current = current.pointers[letter_index]	 # tread along the node (for the current word, regardless of whether it is max) 
			current.num_cNode += 1
			
			if i == len(word) - 1:	# if last letter
				current.pointers[26] = '$'	 # last position to store $	   
				current.max_cNode = 26
				current.max_cNode_freq = freq
				current.descp = descp		 # description of *This* word. Only at last node with '$'
				
	def suggestWord(self, prefix):		# WRONG *TO DO: pick smallest between list of same biggest freq 
		# WRONG *e.g. 'an' should output 'antimask' instead of 'annumerate' if these have max, equal freq. Note: it's not.
		# Should do "Alphabetically" smaller
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
			
			# if no child node, but word exists (i.e. prefix is the full word)
			"""
			### Having this allows 'abdominaliasgdg' to go through for some reason (but other info still correct)
			### EDIT: because you set it to *suggested_word* (which is == prefix)
			### 	but if we disable this block, even though suggested_word is still abdominaliasgdg, it won't get though
			###		since it will continue searching None node (result in return notfound), rather than return with incorrect result (prefix)
			### QUESTION: How do you keep suggesting *correct result* even with the intelligible excess
			temp = [None]*26 + ['$']
			if current.pointers == temp:	# we always insert something onto the array => never have [None]*27
				return suggested_word, current.max_cNode_freq, current.descp, current.num_cNode
			"""
				
		# go through trie to extract best word. If we reach this point, it's guaranteed we can go on
			# so we don't have to worry about the word not in Trie (since at this point, it's no longer dependent on input prefix)
			# This probably means, when inserting letters, we probably don't have to assign the frequency to each passing node except the last one
			# Well, actually, no. We need it in case there's a word with same prefix but different freq. We need a way to compare without having
				# to go all the way down to get the freq of the existing word.
			# Also, max freq of parent and another child node may not be the same in case child node is less freq. 
			# If the prefix goes down to the child node, we need the max freq up to which affects the child node, not of the parent's freq
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
			
				
	##########################################################################
	def searchWord(self, word):
		"""
		return True if there's word in trie. Otherwise, return Flase
		"""
		current = self.root
		for i in range(len(word)):
			
			s_letter_index = ord(word[i]) - 97	# letter index to search in trie
			try:
				if current.pointers[s_letter_index] is None:
					return False	# not found
			except IndexError:	# if length of word exceed the length available word in trie
				return False
				
			current = current.pointers[s_letter_index]	 # if not None: there's a Node in this position of array
			if i == len(word) - 1:
				try:
					if current.pointers[26] == '$':
						return True
				except IndexError:
					pass
				except TypeError:	# 'NoneType' object is not subscriptable
					pass
					
		return False	# not end with $
		
	"""
	def deleteWord(self, word):
	"""
		# delete word from trie. True if successful, False if word not in trie
	"""
		current = self.root
		for i in range(len(word)):
			s_letter_index = ord(word[i]) - 97
			if current.pointers[s_letter_index] is None:
				return False	# not found
			current = current.pointers[s_letter_index]
			if i == len(word) - 1:
				try:
					if current.pointers[26][0] == '$':
						current.pointers[26] = None		# delete $ => no word. This is the only diff to search
						return True
				except IndexError:
					pass
		return False	# not end with $	  
	""" 
	############################################################################
		
	
	
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
	
	print(trie_words.searchWord('abnormally'))
	
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

		
	  
	