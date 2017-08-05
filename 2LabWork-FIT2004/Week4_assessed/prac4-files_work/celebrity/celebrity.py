def tw_celebrity(user):
    """
    Find all kth celebrities on Twitter based on the number of followers
    in O(k) space and O(Nlogk) time
    
    """
    f = open(user,'r')
    N_k = f.readline()
    N_k = N_k.split()
    N = int(N_k[0])
    k = int(N_k[1])
    
    # Sorting by python takes O(NlogN) time
    # if apply with k, it will take O(klogk) time
    
    celeb = []  # list of celebrities
    line = int(f.readline())
    # follower first since we want to primarily sort follower
    
    ID = 1      # id starts from 1, but first id already in list
    for line in f:
        follower = int(line)
        if len(celeb) < k:     # if there're still rooms to fill 
            #if follower >= celeb[-1][0]:    # if more/eq follower to least popular celeb (tale = since still room to fill)
            celeb.append((follower, ID*-1))  # *-1 so it sorts id in ascending order if remove -
            celeb.sort(reverse=True)
        elif len(celeb) >= k:   #>= (NOT >)!
            # celeb with equal follower to least popular celeb will have greater ID, so don't take
            if follower > celeb[-1][0]:
                celeb[-1] = (follower, ID*-1)
                celeb.sort(reverse=True)
        ID += 1
        
    for i in range(len(celeb)):
        print(i+1, celeb[i][-1]*-1, celeb[i][0])
    
    
tw_celebrity('testdata.txt')
