import math
import timeit

inputfile = open('testdata.txt')
line = inputfile.readline()
line = line.strip()
line = line.split()
N = int(line[0])
k = int(line[1])
array = []

start= timeit.default_timer()
ID = 1
for line in inputfile:
    followers = int(line)
    array.append((followers,ID*-1))
    ID +=1
    
array.sort() # this takes O(N log N)


rank = 1
for i in range(N-1,N-k-1,-1):
    print(rank,array[i][1]*-1,array[i][0])
    rank += 1
    

stop= timeit.default_timer()


# uncomment the print command to print the time this program takes
#print(stop-start)  
