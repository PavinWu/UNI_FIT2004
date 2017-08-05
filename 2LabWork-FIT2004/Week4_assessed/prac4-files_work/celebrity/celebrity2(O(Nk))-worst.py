def tw_celebrity(user):
    """
    Find all kth celebrities on Twitter based on the number of followers
    in O(k) space and O(Nlogk) time
    
    It's O(Nlogk). So it bounds O(N), O(k), O(logN), O(logk), O(klogk).
    ...
    BUT Not bound O(Nk)
    """
    f = open(user,'r')
    N_k = f.readline()
    N_k = N_k.split()
    N = int(N_k[0])
    k = int(N_k[1])
    
    # Sorting by python takes O(NlogN) time
    # if apply with k, it will take O(klogk) time
    
    celeb = []  # list of celebrities
    line = int(f.readline())*(-1)       
        # *(-1) because binary search assume list sorted ascendingly, but 
        # we want greater number first
    celeb.append((line, 1))      # follower line, ID 1
        # follower first since we want to primarily sort follower
    
    ID = 2      # id starts from 1, but first id already in list
    for line in f:
        follower = int(line)*(-1)
        #print(celeb, len(celeb) , (follower, ID))    ###
        i_to_insert = binary_closest_tuple(celeb, (follower, ID))
        #print('i to insert is ' + str(i_to_insert))  ###
        if len(celeb) < k:
            celeb.insert(i_to_insert, (follower, ID))  # This takes O(k)
        else:
            if i_to_insert <= k:
                celeb.insert(i_to_insert, (follower, ID))
                celeb.pop()     # to keep celeb within k
            
        ID += 1
        
    for i in range(len(celeb)):
        print(i+1, celeb[i][-1], celeb[i][0]*(-1))
    
def binary_closest_tuple(ls, num):
    """
    Get the closest number to num in the list ls.
    Assume each element in ls is a tuple
    
    """
    lo = 0
    hi = len(ls)
    
    while lo < hi - 1:
        mid = (lo+hi)//2
        if num[0] >= ls[mid][0]:
            lo = mid
        else:
            hi = mid
    
    # if num is same as first, and there's only one first: insert 0 + 1
    #   i.e. insert later due to greater ID
    # if num is greater than first, insert 0
    #   i.e. insert first due to more follower
    # only affect if have to insert to first element! WHY???

    if len(ls) <= 1:
        if num[0] == ls[0][0] or num[0] > ls[0][0]: 
            return lo + 1
        else:   # num[0] < ls[0][0]:
            return lo
        
    if lo == 0:
        if num[0] >= ls[0][0]: # i.e. new celeb has follower <= first celeb 
            return lo + 1
        elif num[0] < ls[0][0]: # i.e. new celeb has follower > first celeb
            return lo
        # WRONG: [no need for >, since as len(ls) > 1, num[0] > ls[0][0] will not be 0]
        # it will be if it is meant to be the second largest in celeb list (still got bumped to 0)
    else:
        return lo + 1   # always be number closest to middle. 
    
    # if ID is ascending (which it is), it will end up in correct position
    # Assuming #follower is turned to negative
    # so instead of having to go to front for number to align, going to back already align itself.
    
#print(binary_closest_tuple([(-10,7),(-9,8),(-8,1),(-6,3),(-6,4),(-4,2),(-3,5),(-2,6)],(-3,20)))
#print(binary_closest_tuple([(-10,7)],(-11,20)))
    
tw_celebrity('testdata.txt')
