def playlist():
    f = open('songs.txt', 'r')
    N = int(f.readline())
    songs_dur = f.readline().split()    # Each item in this list is a string!
    for i in range(len(songs_dur)):
        songs_dur[i] = int(songs_dur[i])    # convert them to int
    
    T = 14    # Duration of Alice's travel
   
    ## FINDING SOLUTION
    possible_dur_soln = []   # a matrix which contains incresing T in each row, i in each col
    # This will contain the sub-solutions to sub-problem associated with each song
    
    for i in range(T):
        possible_dur_soln.append([0]*(N+1))       # create matrix of 0's 
        
    for n in range(N):     # we need to take account additional column of 0's
        for t in range(T):
            dur_sum = songs_dur[n] + (t+1)*possible_dur_soln[t][n]  
            if dur_sum <= T:            # Check and put to next col
                possible_dur_soln[dur_sum-1][n+1] = 1     # change state of entry with matching T
            # index of T's starts from 0, but T starts from 1
            # n starts from 0 (as songs in songs_dur), but the column with non-zero duration starts from 1.
        for t in range(T):  # copy over 1's from just previous column      
            if possible_dur_soln[t][n] == 1:
                possible_dur_soln[t][n+1] = 1   # This exists, but n in for loop don't go there => no ref error
        
    ## BACKTRACK
    song_list_id = []
    dur_bt = 0      # value
    dur_bt_n = 0    # col
    n = 0 
    
    while n <= N and dur_bt == 0:
        if possible_dur_soln[T-1][n] == 1:
            dur_bt_n = n
            dur_bt = T  ####
            song_list_id.append(dur_bt_n)
        n += 1
        
    if dur_bt == 0:
        print('Bad luck Alice! Hahaha!')
        return
    else: 
        dur_bt -= songs_dur[dur_bt_n - 1]
        dur_bt_n -= 1
        
        while dur_bt_n > 0 and dur_bt > 0:
            
            if possible_dur_soln[dur_bt - 1][dur_bt_n - 1] != 1:    # value-1: offset, col-1: see left (not offset)
                
                song_list_id.append(dur_bt_n)   # id starts from 1, as col
                dur_bt -= songs_dur[dur_bt_n - 1] # but there's offset in songs duration list
                
            dur_bt_n -= 1
    
    song_list_id = reverse(song_list_id)    
    for id in song_list_id:
        print("ID: " + str(id) + " Duration: " + str(songs_dur[id-1]))  # ID's are offset by +1 in songs_dur
    
    return possible_dur_soln
    
def reverse(list):
    l = len(list)
    for i in range(l//2):
        list[i], list[l-i-1] = list[l-i-1], list[i]
    return list
            
if __name__ == "__main__":
    playlist()
        