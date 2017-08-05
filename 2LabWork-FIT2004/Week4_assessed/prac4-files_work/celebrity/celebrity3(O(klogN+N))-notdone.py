from heapq import heappush, heappop, heapify
    
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
    
    celeb = []  # list of celebrities
    
    ID = 1
    for line in f:
        celeb.append((int(line)*-1, ID))
        """
        follower = int(line)*(-1)
        if len(celeb) < k:
            heappush(celeb, (follower, ID))
            
            
        else:
            if i_to_insert <= k:
                celeb.insert(i_to_insert, (follower, ID))
                celeb.pop()     # to keep celeb within k
        """    
        ID += 1
        
    heapify(celeb)  # takes O(N) (according to doc)

    for i in range(k):  # takes klogN
        celeb_i = heappop(celeb)    
        print(i+1, celeb_i[-1], celeb_i[0]*(-1))
    
tw_celebrity('testdata.txt')
