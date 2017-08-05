def trie_generate(alphabet_size):
    """
    generate a trie of English alphabet
    """
    return [None]*alphabet_size
   
    
def trie_insertWord(trie, word):
    """
    Insert the input string into the input Retrieval tree
    @ pre-condition: the word must end with $
    @ pre-condition: the word consists only of lower case English alphabets
    """
    for i in range(len(word)-1):
        letter_index = ord(word[i]) - 97   # ASCII of 1st word - 97     # 97: first English char in ASCII is 'a' with value 97)
        if trie[letter_index] is None:
            next_letter_index = ord(word[i+1]) - 97
            trie[letter_index] = [next_letter_index]    # insert a sub-array
        else:
            next_letter_index = ord(word[i+1]) - 97
            trie[letter_index].append(next_letter_index)
            if i == len(word) - 2:   # if reaches last letter
                if trie[next_letter_index] is None:
                    trie[next_letter_index] = ['$']
                else:
                    trie[next_letter_index].append('$')
    
#def trie_deleteWord():

#def trie_searchWord():


if __name__ == "__main__":
    trie = trie_generate(26)
    words = ['rubicundus', 
             'romulus',
             'romane',
             'rubicon',
             'ruber',
             'romanus',
             'rubens']
    #print(trie)
    for word in words:
        trie_insertWord(trie, word)
    i = 0
    for item in trie:
        print(i, chr(i+97), item)
        i += 1
    