from heapq import heappush, heappop
    
def tw_celebrity(tw_user):
    """
    Find all kth celebrities on Twitter based on the number of followers
    in O(k) space and O(Nlogk) time
    
    This is slower than O(Nklogk) algoeithm for some reasons.
    It's even slower than naive.py.
    """
    f = open(tw_user,'r')
    N_k = f.readline()
    N_k = N_k.split()
    N = int(N_k[0])
    k = int(N_k[1])
    
    celeb = []  # list of celebrities
    
    ID = 1
    for line in f:
        heappush(celeb, (int(line), -1*ID))
        if len(celeb) > k:
                heappop(celeb)
        ID += 1
        
    celeb.sort(reverse=True)    # takes O(klogk)
    
    for i in range(k):  
        print(i+1, celeb[i][-1]*-1, celeb[i][0])
    
tw_celebrity('testdata.txt')
