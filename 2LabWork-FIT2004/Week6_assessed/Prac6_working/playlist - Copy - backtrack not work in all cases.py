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
        # (so we don't have to deal with different list size in loop below)
        # + 1 because we also have a column of 0 (for 1st non-zero col to add) 
        
    for i in range(N):     # we need to take account additional column of 0's
        for t in range(T):
            dur_sum = songs_dur[i] + (t+1)*possible_dur_soln[t][i]  # Check and put to next col
            if dur_sum <= T:
                possible_dur_soln[dur_sum-1][i+1] = 1     # change state of entry with matching T
            # dur_sum-1???:
                # index of T's starts from 0, but T starts from 1
                # The sum will correspond to T. Since we use sum to refer to index (not T itself), we 
                # need to subtract by 1.
            # i+1?:
                # i starts from 0, as well as index of the entries in songs_dur
                # , but in the matrix, the column with non-zero duration starts from 1.
        for t in range(T):  # copy over 1's from just previous column      
            if possible_dur_soln[t][i] == 1:
                possible_dur_soln[t][i+1] = 1
                
    for i in range(len(possible_dur_soln)):
        print('{:<2}'.format(i), possible_dur_soln[i])   # cool way to format
        
        
    ## BACKTRACK
    
    song_list_id = []
    dur_bt = 0      # store the duration (for backtracking)
    dur_bt_i = 0    # store the index at which the duration is found
    n = 0           # n to count. We have N songs => N-1 is last index if start from 0. But we also have col of 0.
    while n <= N and dur_bt == 0:    # Set i to be the index of column. We'll never use the first 0's column.
        if possible_dur_soln[T-1][n] == 1:  # search if possible to get song of duration T-1. This is a SETUP stage (no backtrack yet)
            dur_bt_i = n
            dur_bt = T-1            ## TAKE OUT THIS -1 AND  ADJUST ACCORDINGLY BELOW (easier to think this way). This fixes the bug      
                                    # at *index* of row corresponding to T i.e. T-1
            song_list_id.append(dur_bt_i)
        n += 1      # The bug this code fixes won't show with current test case! (i.e. if last is not 1)
    if dur_bt == 0:
        print('Bad luck Alice! Hahaha!')
        return
    else:       # start backtrack here
        dur_bt -= songs_dur[dur_bt_i - 1]   # dur_soln_i is offset by +1 (if we want to start from 0)
        dur_bt_i -= 1         # go to left col (this subtraction is NOT due to offset)
        while dur_bt_i > 0 and dur_bt > 0:
            # print(possible_dur_soln[dur_soln][dur_soln_i - 1])  ###
            if possible_dur_soln[dur_bt][dur_bt_i - 1] != 1:    # look at left of this left (now current) col
                song_list_id.append(dur_bt_i)
                print("song duration:", songs_dur[dur_bt_i - 1])    ###
                dur_bt -= songs_dur[dur_bt_i - 1] - 1    # This has -1 offset from actual difference
                # Note: There is always 1 in this position, since we extracted 1 from it when finding the solution 
                print(dur_bt_i, dur_bt) ###
            dur_bt_i -= 1   # if there is 1 on left, go left again (as it means we get this soln by copying from left)
            # otherwise update dur_soln and append the index of song into song_list
    
    song_list_id = reverse(song_list_id)    
    for id in song_list_id:
        print("ID: " + str(id) + " Duration: " + str(songs_dur[id-1]))  # ID's are offset by +1
    
    return possible_dur_soln
    
def reverse(list):
    l = len(list)
    for i in range(l//2):
        list[i], list[l-i-1] = list[l-i-1], list[i]
    return list
            
if __name__ == "__main__":
    playlist()
    #playlist_matrix = playlist()
    #for i in range(len(playlist())):   # for fun
    #for i in range(len(playlist_matrix)):
    #    print('{:<2}'.format(i), playlist_matrix[i])   # cool way to format
        