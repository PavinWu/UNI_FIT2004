import math
import bisect

inputfile = open('testdata.txt')

Numbers=[]
tot = 0
for line in inputfile:
    num = int(line)
    tot += 1
        
    bisect.insort(Numbers,num) # insert the incoming number in sorted order: takes O(N)
    
    
    if tot % 2 == 0:
        index = int(tot/2)
        index -=1
        median = (Numbers[index] + Numbers[index + 1])/2
    else:
        index = int((tot+1)/2)
        index -=1
        median = Numbers[index]

    # The following if block prints the total number of integers read so far (after every 10,000
    # This is useful when you are testing naive.py for very large input file as it will show you the progress.
    if tot % 10000 == 0:
        print(tot)

    # You may want to comment the following print command if you are using large input file
    print(int(median))
    
