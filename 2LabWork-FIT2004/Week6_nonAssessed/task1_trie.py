
class trieNode:
    def __init__(self):     # This is how you initiate multiple "attributes" to one thing: OO
        #self.weight = 0     # how many pointers in this node?   can be used for deletion!
        self.pointers = [None]*27   # 27 for $. Can improve?
      
class trie:
    def __init__(self):
        self.root = trieNode()
        
    def insertWord(self, word):
        """
        insert word into trie
        """
        current = self.root
        for i in range(len(word)):
            letter_index = ord(word[i]) - 97
            if current.pointers[letter_index] is None:
                #current.weight += 1
                current.pointers[letter_index] = trieNode()
            current = current.pointers[letter_index]     # if not None, just go further down the node
            if i == len(word) - 1:  # if last letter
                #current.weight += 1
                current.pointers[26] = '$'   # last position to store $     
    
    def searchWord(self, word):
        """
        return True if there's word in trie. Otherwise, return Flase
        """
        current = self.root
        for i in range(len(word)):
            s_letter_index = ord(word[i]) - 97  # letter index to search in trie
            if current.pointers[s_letter_index] is None:
                return False    # not found
            current = current.pointers[s_letter_index]   # if not None: there's a Node in this position of array
            if i == len(word) - 1:
                if current.pointers[26] == '$':
                    return True
        return False    # not end with $
        
    def deleteWord(self, word):
        """
        delete word from trie. True if successful, False if word not in trie
        """
        
        current = self.root
        for i in range(len(word)):
            s_letter_index = ord(word[i]) - 97
            if current.pointers[s_letter_index] is None:
                return False    # not found
            current = current.pointers[s_letter_index]
            if i == len(word) - 1:
                if current.pointers[26] == '$':
                    current.pointers[26] = None     # delete $ => no word. This is the only diff to search
                    return True
        return False    # not end with $

        """
        # delete prematurely
        current = self.root
        for i in range(len(word)):
            s_letter_index = ord(word[i]) - 97
            if current.pointers[s_letter_index] is None:
                print(i)
                return False    # not found
            temp = current.pointers[s_letter_index]
            if current.weight < 2:
                current.pointers[s_letter_index] = None
                current.weight -= 1
                return True
            current = temp
            if i == len(word) - 1:
                if current.pointers[26] == '$':
                    current.pointers[26] = None     # delete $ => no word. This is the only diff to search
                    current.weight -= 1
                    return True
        return False    # not end with $
        """
    
    """
    def printWords(self):
        current = self.root
        self._aux_printWords(current)
        
    def _aux_printWords(self, current):
        for i in range(len(current.pointers)):
            if current.pointers is not None:                    
                if current.pointers[26] == '$':
                   return ''
                else:
                   return a_word[0] + self._aux_printWords(current.pointers[letter_index], a_word[1:])
    """            
        
        
if __name__ == "__main__":
    words = ['rubicundus', 'romulus', 'romane', 'rubicon', 'ruber', 'romanus', 'rubens', 'asdd']
    trie_task1 = trie()
    
    # test insertWord
    for word in words:
        trie_task1.insertWord(word)
    
    # test searchWord
    for word in words:
        print(trie_task1.searchWord(word))
    
    print()
    # test deleteWord
    print(trie_task1.deleteWord(words[1]))
    print(trie_task1.searchWord(words[1]))
    
    # test printWords
    
      
    