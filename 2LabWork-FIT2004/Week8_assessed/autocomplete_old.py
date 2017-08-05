
class trieNode:
    def __init__(self):     # This is how you initiate multiple "attributes" to one thing: OO
        #self.weight = 0     # how many pointers in this node?   can be used for deletion!
        self.pointers = [None]*27   # 27 for $. Can improve?
        self.max_node = (0,0)   # (letter index which gives max_freq, max_freq)
        # when search. Only have to look at max_freq at the first start 
      
class trie:
    def __init__(self):
        self.root = trieNode()
        
    def insertWord(self, word, freq, descp):
        """
        insert word into trie
        """
        current = self.root
        for i in range(len(word)):
            letter_index = ord(word[i]) - 97
            
            if current.pointers[letter_index] is None:      # if no word, update max node
                current.pointers[letter_index] = trieNode()
            
            if current.max_node[1] < freq:
                current.max_node = (letter_index, freq)
            current = current.pointers[letter_index]     # if not None, just go further down the node
            
            if i == len(word) - 1:  # if last letter
                current.max_node = 26
                current.pointers[26] = ('$', freq, descp)   # last position to store $     
                
    
    def searchWord(self, word):
        """
        return True if there's word in trie. Otherwise, return Flase
        """
        current = self.root
        for i in range(len(word)):
            s_letter_index = ord(word[i]) - 97  # letter index to search in trie
            try:
                if current.pointers[s_letter_index] is None:
                    return False    # not found
            except IndexError:  # if length of word exceed the length available word in trie
                return False
            current = current.pointers[s_letter_index]   # if not None: there's a Node in this position of array
            if i == len(word) - 1:
                try:
                    if current.pointers[26][0] == '$':
                        return True
                except IndexError:
                    pass
                except TypeError:   # 'NoneType' object is not subscriptable
                    pass
        return False    # not end with $
        
    """
    def deleteWord(self, word):
    """
        # delete word from trie. True if successful, False if word not in trie
    """
        current = self.root
        for i in range(len(word)):
            s_letter_index = ord(word[i]) - 97
            if current.pointers[s_letter_index] is None:
                return False    # not found
            current = current.pointers[s_letter_index]
            if i == len(word) - 1:
                try:
                    if current.pointers[26][0] == '$':
                        current.pointers[26] = None     # delete $ => no word. This is the only diff to search
                        return True
                except IndexError:
                    pass
        return False    # not end with $      
    """ 
        
if __name__ == "__main__":
    trie_words = trie()
    
    f = open('Dictionary.txt', 'r')
    i = 0
    for line in f:
        if line != '\n':           # if not empty line   
            if i == 0:
                word = line[6:].rstrip()    # don't take 'word: ', then strip off '/n'
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
        
        
      
    